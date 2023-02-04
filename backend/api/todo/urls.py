from django.urls import path

from api.todo import views

urlpatterns = [
    path('record/list', views.TodoListRecordView.as_view(), name="record-list"),
    path('record/all', views.TodoAllRecordView.as_view(), name="record-all"),
    path('record/create', views.TodoCreateRecordView.as_view(), name="record-create"),
    path('record/get', views.TodoGetRecordView.as_view(), name="record-get"),
    path('record/delete', views.TodoDeleteRecordView.as_view(),name="record-delete"),
]
