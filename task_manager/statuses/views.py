from django.forms import Form
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from task_manager.mixins import LoginRequireMixin
from task_manager.views import CreateFlashedView, UpdateFlashedView, DeleteFlashedView


class StatusAbstractMixin(LoginRequireMixin):
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')


class StatusIndexView(StatusAbstractMixin, ListView):
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'
    ordering = ['pk']


class StatusCreateView(StatusAbstractMixin, CreateFlashedView):
    template_name = 'statuses/create.html'
    valid_form_message = _('Status has been created successfully.')


class StatusUpdateView(StatusAbstractMixin, UpdateFlashedView):
    template_name = 'statuses/update.html'
    valid_form_message = _('Status has been updated successfully.')


class StatusDeleteView(StatusAbstractMixin, DeleteFlashedView):
    template_name = 'statuses/delete.html'
    redirect_url = reverse_lazy('statuses')
    success_url = reverse_lazy('statuses')
    valid_data_message = _('Status has been deleted successfully.')
    invalid_data_message = _('Cannot delete status because it is in use.')
    form_class = Form

    def post(self, request, *args, **kwargs):
        status = Status.objects.get(pk=kwargs['pk'])
        if status.tasks.first():
            self.is_correct_data = False
        return super().post(request, *args, **kwargs)
