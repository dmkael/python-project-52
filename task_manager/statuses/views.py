from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from task_manager.mixins import LoginRequireMixin


# Create your views here.
class StatusIndexView(LoginRequireMixin, ListView):
    model = Status
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'
    ordering = ['pk']


class StatusCreateView(LoginRequireMixin, CreateView):
    model = Status
    template_name = 'statuses/create.html'
    form_class = StatusForm
    success_url = reverse_lazy('statuses')

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('Status has been created successfully.')
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=400)


class StatusUpdateView(LoginRequireMixin, UpdateView):
    model = Status
    template_name = 'statuses/update.html'
    form_class = StatusForm
    success_url = reverse_lazy('statuses')

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('Status has been updated successfully.')
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=400)


class StatusDeleteView(LoginRequireMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses')

    def get_success_url(self):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('Status has been deleted successfully.'))
        return super().get_success_url()
