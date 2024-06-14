from django.forms import Form
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label
from task_manager.view_mixins import (
    CreateViewMixin,
    UpdateViewMixin,
    DeleteViewMixin,
    IndexViewMixin
)
from task_manager.access_mixins import LoginRequireMixin


# Create your views here.
class LabelAbstractMixin(LoginRequireMixin):
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels')


class LabelIndexView(LabelAbstractMixin, IndexViewMixin):
    extra_context = {
        'url_name': 'label_create',
        'header': _('Labels'),
        'button_text': _('Create label')
    }
    template_name = 'labels/index.html'
    context_object_name = 'labels'
    ordering = ['pk']


class LabelCreateView(LabelAbstractMixin, CreateViewMixin):
    extra_context = {'button_text': _('Create'), 'header': _('Create label')}
    template_name = 'labels/create.html'
    success_message = _('Label has been created successfully.')


class LabelUpdateView(LabelAbstractMixin, UpdateViewMixin):
    extra_context = {'button_text': _('Edit'), 'header': _('Edit label')}
    template_name = 'labels/update.html'
    success_message = _('Label has been updated successfully.')


class LabelDeleteView(LabelAbstractMixin, DeleteViewMixin):
    extra_context = {'button_text': _('Yes, delete'), 'header': _('Delete label')}
    template_name = 'labels/delete.html'
    success_message = _('Label has been deleted successfully.')
    failure_message = _('Cannot delete label because it is in use.')
    redirect_url = reverse_lazy('labels')
    form_class = Form

    def post(self, request, *args, **kwargs):
        label = Label.objects.get(pk=kwargs['pk'])
        if label.tasks.first():
            self.have_dependencies = True
        return super().post(request, *args, **kwargs)
