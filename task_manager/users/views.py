from django.contrib import messages
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from task_manager.users.forms import UserForm
from task_manager.users.mixins import UserCreatorOnlyMixin


class UsersAbstractMixin:
    model = get_user_model()
    success_url = reverse_lazy('users')
    form_class = UserForm


class UsersIndexView(UsersAbstractMixin, ListView):
    template_name = 'users/index.html'
    context_object_name = 'users'
    ordering = ['pk']


class UserCreateView(UsersAbstractMixin, CreateView):
    template_name = 'users/create.html'

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('User has been registered successfully.')
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=400)


class UserUpdateView(UserCreatorOnlyMixin, UsersAbstractMixin, UpdateView):
    template_name = 'users/update.html'

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('User has been updated successfully.')
        )
        response = super().form_valid(form)
        update_session_auth_hash(self.request, form.instance)
        return response

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=400)


class UserDeleteView(UserCreatorOnlyMixin, UsersAbstractMixin, DeleteView):
    template_name = 'users/delete.html'

    def post(self, request, *args, **kwargs):
        user = get_user_model().objects.get(pk=request.user.id)
        if user.tasks_author.first() or user.tasks_executor.first():
            messages.add_message(
                self.request,
                messages.ERROR,
                _('Cannot delete user because it is in use.')
            )
            return redirect(reverse_lazy('users'))
        user.delete()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('User has been deleted successfully.'))
        return redirect(self.success_url)
