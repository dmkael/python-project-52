from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
from .mixins import AuthorizedOnlyMixin
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from task_manager.users.forms import UserCreationForm
from django.utils.translation import gettext as _


class UsersIndexView(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all().order_by('pk')
        return render(request, 'users/users_index.html', context={'users': users})


class UserCreateView(CreateView):

    model = User
    form_class = UserCreationForm
    template_name = 'users/create.html'

    def get_success_url(self):
        return reverse('login')

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('User has been registered successfully.')
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=400)


class UserUpdateView(AuthorizedOnlyMixin, UpdateView):

    model = User
    form_class = UserCreationForm
    template_name = 'users/update.html'

    def get_success_url(self):
        return reverse('users')

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('User has been updated successfully.')
        )
        response = super().form_valid(form)
        update_session_auth_hash(self.request, self.get_object())
        return response

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=400)


class UserDeleteView(AuthorizedOnlyMixin, DeleteView):

    model = User
    template_name = 'users/delete.html'

    def get_success_url(self):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('User has been deleted successfully.'))
        return reverse('users')
