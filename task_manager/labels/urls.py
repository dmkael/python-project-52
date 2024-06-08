from django.urls import path
from task_manager.labels.views import (
    LabelIndexView,
    LabelCreateView,
    LabelUpdateView,
    LabelDeleteView
)

urlpatterns = [
    path('create/', LabelCreateView.as_view(), name='label_create'),
    path('<int:pk>/update/', LabelUpdateView.as_view(), name='label_update'),
    path('<int:pk>/delete/', LabelDeleteView.as_view(), name='label_delete'),
    path('', LabelIndexView.as_view(), name='labels'),
]
