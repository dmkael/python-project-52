from django.urls import path
from task_manager.tasks.filters import TasksFilter
from task_manager.tasks.views import (
    TaskIndexView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
)

urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('', TaskIndexView.as_view(), name='tasks'),
]
