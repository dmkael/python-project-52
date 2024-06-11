from django.forms import Form
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _
from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label
from task_manager.view_mixins import (
    CreateFlashedView,
    UpdateFlashedView,
    DeleteFlashedView
)
from task_manager.access_mixins import LoginRequireMixin


# Create your views here.
class LabelAbstractMixin(LoginRequireMixin):
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels')


class LabelIndexView(LabelAbstractMixin, ListView):
    template_name = 'labels/index.html'
    context_object_name = 'labels'
    ordering = ['pk']


class LabelCreateView(LabelAbstractMixin, CreateFlashedView):
    template_name = 'labels/create.html'
    success_message = _('Label has been created successfully.')


class LabelUpdateView(LabelAbstractMixin, UpdateFlashedView):
    template_name = 'labels/update.html'
    success_message = _('Label has been updated successfully.')


class LabelDeleteView(LabelAbstractMixin, DeleteFlashedView):
    template_name = 'labels/delete.html'
    success_message = _('Label has been deleted successfully.')
    failure_message = _('Cannot delete label because it is in use.')
    redirect_url = reverse_lazy('labels')
    success_url = reverse_lazy('labels')
    form_class = Form

    def post(self, request, *args, **kwargs):
        label = Label.objects.get(pk=kwargs['pk'])
        if label.tasks.first():
            self.have_dependencies = True
        return super().post(request, *args, **kwargs)
