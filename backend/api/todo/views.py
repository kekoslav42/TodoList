from django.contrib.auth.models import Permission
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiResponse, \
    OpenApiParameter
from rest_framework import generics, exceptions, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from api.todo.filters import TodoListRecordFilter
from api.todo.serializers.common import TodoSerializer
from apps.todo.models import TodoRecord


class BaseTodoRecordView(APIView):
    """ Base APIView to delete and retrieve methods with using query_filters """
    permission_classes = [permissions.AllowAny]
    serializer_class = TodoSerializer
    queryset = TodoRecord.objects.all()

    def get_object(self) -> TodoRecord:
        """
            Get the todo record using the provided UUID.
        """
        uuid = self.request.GET.get('uuid', None)
        if uuid is None:
            raise exceptions.ValidationError({"msg": "uuid is required"})
        todo = self.queryset.filter(uuid=uuid)
        if not todo.exists():
            raise exceptions.NotFound({"msg": "404 Not Found"})
        return todo.first()


@extend_schema(tags=['Задачи', ])
@extend_schema_view(
    get=extend_schema(
        operation_id="get_todos_with_filter",
        summary="Get todos with filters",
        description="Getting all tasks by filter with date fields start= and end=, "
                    "if the fields are not passed, all records will be displayed.",
    )
)
class TodoListRecordView(generics.ListAPIView):
    """
        View to list all todo records.
    """
    permission_classes = [permissions.AllowAny]
    queryset = TodoRecord.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = TodoListRecordFilter


@extend_schema(tags=['Задачи', ])
@extend_schema_view(
    get=extend_schema(
        operation_id="get_all_todos",
        summary="Get todos",
        description="Getting all todo without filters."
    )
)
class TodoAllRecordView(generics.ListAPIView):
    """
        View to list all todo records.
    """
    permission_classes = [permissions.AllowAny]
    queryset = TodoRecord.objects.all()
    serializer_class = TodoSerializer


@extend_schema(tags=['Задачи', ])
@extend_schema_view(
    post=extend_schema(
        operation_id="create_todo",
        summary="Create todo",
        description="Create a new todo with the given parameters."
    )
)
class TodoCreateRecordView(generics.CreateAPIView):
    """
        View to create new todo records.
    """
    permission_classes = [permissions.AllowAny]
    queryset = TodoRecord.objects.all()
    serializer_class = TodoSerializer


@extend_schema(tags=['Задачи', ])
@extend_schema_view(
    delete=extend_schema(
        operation_id="delete_todo",
        summary="Delete todo",
        description="Deleting todo with uuid",
        parameters=[
            OpenApiParameter(name='uuid', description='uuid', type=str),
        ]
    )
)
class TodoDeleteRecordView(BaseTodoRecordView):
    """
        View to delete a todo record.
    """

    def delete(self, request, *args, **kwargs) -> Response:
        """
            Delete a todo record.
        """
        todo = self.get_object()
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema(tags=['Задачи', ])
@extend_schema_view(
    get=extend_schema(
        operation_id="get_todo",
        summary="Get todo",
        description="Getting todo by its uuid.",
        parameters=[
            OpenApiParameter(name='uuid', description='uuid', type=str),
        ]
    )
)
class TodoGetRecordView(BaseTodoRecordView):
    """
        View to retrive a todo record.
    """

    def get(self, request, *args, **kwargs) -> Response:
        """
            Retrieve a todo record.
        """
        todo = self.get_object()
        serializer = self.serializer_class(todo, many=False)
        return Response(serializer.data, status=200)
