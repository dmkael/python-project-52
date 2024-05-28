from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.utils.translation import activate


class UsersIndexView(View):

    def get(self, request):
        users = User.objects.all()
        return render(request, 'users/users_index.html', context={'users': users})
