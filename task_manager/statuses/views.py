from django.forms import Form
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from task_manager.access_mixins import LoginRequireMixin
from task_manager.view_mixins import (
    CreateViewMixin,
    UpdateViewMixin,
    DeleteViewMixin,
    IndexViewMixin
)


class StatusAbstractMixin(LoginRequireMixin):
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')


class StatusIndexView(StatusAbstractMixin, IndexViewMixin):
    extra_context = {
        'header': _('Statuses'),
        'button_url': reverse_lazy('status_create'),
        'button_text': _('Create status')
    }
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'
    ordering = ['pk']


class StatusCreateView(StatusAbstractMixin, CreateViewMixin):
    extra_context = {'button_text': _('Create'), 'header': _('Create status')}
    template_name = 'statuses/create.html'
    success_message = _('Status has been created successfully.')


class StatusUpdateView(StatusAbstractMixin, UpdateViewMixin):
    extra_context = {'button_text': _('Edit'), 'header': _('Edit status')}
    template_name = 'statuses/update.html'
    success_message = _('Status has been updated successfully.')


class StatusDeleteView(StatusAbstractMixin, DeleteViewMixin):
    extra_context = {'button_text': _('Yes, delete'), 'header': _('Delete status')}
    template_name = 'statuses/delete.html'
    success_message = _('Status has been deleted successfully.')
    failure_message = _('Cannot delete status because it is in use.')
    redirect_url = reverse_lazy('statuses')
    form_class = Form

    def post(self, request, *args, **kwargs):
        status = Status.objects.get(pk=kwargs['pk'])
        if status.tasks.first():
            self.have_dependencies = True
        return super().post(request, *args, **kwargs)
