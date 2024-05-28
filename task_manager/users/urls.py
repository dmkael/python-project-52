from django.urls import path

from task_manager.users.views import UsersIndexView

urlpatterns = [
    path('', UsersIndexView.as_view(), name='users'),
]
