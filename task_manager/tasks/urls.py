from django.urls import path
from task_manager.tasks.views import (
    TasksIndexView,
    TasksCreateView,
    TaskDetailView,
    TasksUpdateView,
    TasksDeleteView,
)

urlpatterns = [
    path('create/', TasksCreateView.as_view(), name='task_create'),
    path('<int:pk>/update/', TasksUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TasksDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('', TasksIndexView.as_view(), name='tasks'),
]
