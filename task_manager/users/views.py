from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render, redirect
from django.views import View
from task_manager.users.forms import UserCreationForm


class UsersIndexView(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/users_index.html', context={'users': users})


class UserCreateView(View):

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, 'users/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        return render(request, 'users/create.html', {'form': form})


class UserUpdateView(View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        form = UserCreationForm(instance=user)
        return render(request, 'users/update.html', {'form': form, 'user_id': user_id})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        form = UserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
        return render(request, 'users/update.html', {'form': form, 'user_id': user_id})


class UserDeleteView(View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        return render(request, 'users/delete.html', {'user': user})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        user.delete()
        return redirect('users')