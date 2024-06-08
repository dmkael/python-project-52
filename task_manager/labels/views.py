from django.contrib import messages
from django.db.models import ProtectedError
from django.forms import Form
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _
from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label
from task_manager.mixins import LoginRequireMixin


# Create your views here.
class LabelAbstractView(LoginRequireMixin):
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels')


class LabelIndexView(LabelAbstractView, ListView):
    template_name = 'labels/index.html'
    context_object_name = 'labels'
    ordering = ['pk']


class LabelCreateView(LabelAbstractView, CreateView):
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


class LabelUpdateView(LabelAbstractView, UpdateView):
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


class LabelDeleteView(LabelAbstractView, DeleteView):
    success_url = reverse_lazy('labels')
    redirect_url = reverse_lazy('labels')
    template_name = 'labels/delete.html'
    form_class = Form

    def post(self, request, *args, **kwargs):
        try:
            response = self.delete(request, *args, **kwargs)
            messages.add_message(
                self.request,
                messages.SUCCESS,
                _('Label has been deleted successfully.'))
            return response
        except ProtectedError:
            messages.add_message(
                self.request,
                messages.ERROR,
                _('Cannot delete label because it is in use.')
            )
            return redirect(self.redirect_url)
