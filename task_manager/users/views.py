from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from task_manager.mixins import AuthorizedCreatorOnlyMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from task_manager.users.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class UsersIndexView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'
    ordering = ['pk']
    paginate_by = 15


class UserCreateView(CreateView):

    model = User
    form_class = UserCreationForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('User has been registered successfully.')
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=400)


class UserUpdateView(AuthorizedCreatorOnlyMixin, UpdateView):

    model = User
    form_class = UserCreationForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')

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


class UserDeleteView(AuthorizedCreatorOnlyMixin, DeleteView):

    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')

    def get_success_url(self):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('User has been deleted successfully.'))
        return super().get_success_url()
