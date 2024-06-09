from django.urls import reverse_lazy
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _
from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label
from task_manager.views import CreateFlashedView, UpdateFlashedView, DeleteFlashedView
from task_manager.mixins import LoginRequireMixin


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
    valid_form_message = _('Label has been created successfully.')


class LabelUpdateView(LabelAbstractMixin, UpdateFlashedView):
    template_name = 'labels/update.html'
    valid_form_message = _('Label has been updated successfully.')


class LabelDeleteView(LabelAbstractMixin, DeleteFlashedView):
    template_name = 'labels/delete.html'
    redirect_url = reverse_lazy('labels')
    valid_data_message = _('Label has been deleted successfully.')
    invalid_data_message = _('Cannot delete label because it is in use.')

    def post(self, request, *args, **kwargs):
        label = Label.objects.get(pk=kwargs['pk'])
        if label.tasks.first():
            self.is_correct_data = False
        return super().process(request, label)
