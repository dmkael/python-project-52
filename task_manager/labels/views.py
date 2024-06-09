from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _
from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label
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


class LabelCreateView(LabelAbstractMixin, CreateView):
    template_name = 'labels/create.html'

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('Label has been created successfully.')
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=400)


class LabelUpdateView(LabelAbstractMixin, UpdateView):
    template_name = 'labels/update.html'

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('Label has been updated successfully.')
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=400)


class LabelDeleteView(LabelAbstractMixin, DeleteView):
    template_name = 'labels/delete.html'

    def post(self, request, *args, **kwargs):
        label = Label.objects.get(pk=kwargs['pk'])
        if label.tasks.first():
            messages.add_message(
                self.request,
                messages.ERROR,
                _('Cannot delete label because it is in use.')
            )
            return redirect(reverse_lazy('labels'))
        label.delete()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('Label has been deleted successfully.'))
        return redirect(self.success_url)
