from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from task_manager.mixins import LoginRequireMixin


class StatusAbstractMixin(LoginRequireMixin):
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')


class StatusIndexView(StatusAbstractMixin, ListView):
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'
    ordering = ['pk']


class StatusCreateView(StatusAbstractMixin, CreateView):
    template_name = 'statuses/create.html'

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('Status has been created successfully.')
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=400)


class StatusUpdateView(StatusAbstractMixin, UpdateView):
    template_name = 'statuses/update.html'

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('Status has been updated successfully.')
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=400)


class StatusDeleteView(StatusAbstractMixin, DeleteView):
    template_name = 'statuses/delete.html'

    def post(self, request, *args, **kwargs):
        status = Status.objects.get(pk=kwargs['pk'])
        if status.tasks.first():
            messages.add_message(
                self.request,
                messages.ERROR,
                _('Cannot delete status because it is in use.')
            )
            return redirect(reverse_lazy('statuses'))
        status.delete()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('Status has been deleted successfully.'))
        return redirect(self.success_url)
