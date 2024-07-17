# api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.TodoListCreate.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', views.TodoDetailUpdateDelete.as_view(), name='todo-detail-update-delete'),
]
