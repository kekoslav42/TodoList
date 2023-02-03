from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

from api.todo.filters import TodoListRecordFilter, TodoOneRecordFilter
from api.todo.serializers.common import TodoSerializer
from apps.todo.models import TodoRecord


class TodoListRecordView(generics.ListAPIView):
    queryset = TodoRecord.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = TodoListRecordFilter


class TodoAllRecordView(generics.ListAPIView):
    queryset = TodoRecord.objects.all()
    serializer_class = TodoSerializer


class TodoCreateRecordView(generics.CreateAPIView):
    queryset = TodoRecord.objects.all()
    serializer_class = TodoSerializer


class TodoRecordView(APIView):
    serializer_class = TodoSerializer
    queryset = TodoRecord.objects.all()

    def get_object(self):
        uuid = self.request.GET.get('uuid', None)
        if uuid is None:
            raise exceptions.ValidationError({"msg": "uuid is required"})
        todo = self.queryset.filter(uuid=uuid)
        if not todo.exists():
            raise exceptions.NotFound({"msg": "404 Not Found"})
        return todo.first()

    def delete(self, request, *args, **kwargs):
        todo = self.get_object()
        todo.delete()
        return Response({"msg": f"Object {todo.uuid} successfully deleted"})

    def get(self, request, *args, **kwargs):
        todo = self.get_object()
        serializer = self.serializer_class(todo, many=False)
        return Response(serializer.data, status=200)
