from django.urls import path

from . import views

urlpatterns = [
    path(
        'record/list', views.TodoListRecordView.as_view(), name="record-list"),
    path(
        'record/all', views.TodoAllRecordView.as_view(), name="record-all"),
    path(
        'record/create', views.TodoCreateRecordView.as_view(), name="record-create"),
    path(
        'record/get', views.TodoRecordView.as_view(http_method_names=['get', ]), name="record-get"),
    path(
        'record/delete',
        views.TodoRecordView.as_view(http_method_names=['delete', ]),
        name="record-delete"
    ),
]
