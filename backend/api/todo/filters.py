from django_filters.rest_framework import FilterSet, filters

from apps.todo.models import TodoRecord


class TodoListRecordFilter(FilterSet):
    start = filters.DateFilter(field_name="created", lookup_expr='gte')
    end = filters.DateFilter(field_name="created", lookup_expr='lte')

    class Meta:
        model = TodoRecord
        fields = ['start', 'end']


class TodoOneRecordFilter(FilterSet):
    uuid = filters.CharFilter(field_name="uuid")

    class Meta:
        model = TodoRecord
        fields = ['uuid', ]