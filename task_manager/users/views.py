from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from .mixins import AuthorizedOnlyMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from task_manager.users.forms import UserCreationForm
from django.utils.translation import gettext as _


# def authorized_only(func):
#     @wraps(func)
#     def wrapper(data, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             messages.add_message(
#                 request,
#                 messages.ERROR,
#                 'You are not logged in.'
#             )
#             return redirect('login')
#
#         if request.user.id == kwargs.get('id'):
#             return func(data, request, *args, **kwargs)
#
#         messages.add_message(
#             request,
#             messages.ERROR,
#             "You do not have permission to perform this action."
#         )
#         return redirect('users')
#     return wrapper


class UsersIndexView(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all().order_by('id')
        return render(request, 'users/users_index.html', context={'users': users})


class UserCreateView(View):

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, 'users/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                _('User has been registered successfully.')
            )
            return redirect('login')
        return render(request, 'users/create.html', {'form': form}, status=400)


class UserUpdateView(AuthorizedOnlyMixin, View):

    # @authorized_only
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        form = UserCreationForm(instance=user)
        return render(request, 'users/update.html', {'form': form, 'user_id': user_id})

    # @authorized_only
    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        form = UserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user)
            messages.add_message(
                request,
                messages.SUCCESS,
                _('User has been updated successfully.')
            )
            return redirect('users')
        return render(
            request, 'users/update.html',
            {'form': form, 'user_id': user_id},
            status=400
        )


class UserDeleteView(AuthorizedOnlyMixin, View):

    # @authorized_only
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        return render(request, 'users/delete.html', {'user': user})

    # @authorized_only
    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        user.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            _('User has been deleted successfully.'))
        return redirect('users')
