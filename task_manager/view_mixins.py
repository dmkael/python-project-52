from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib import messages
from django.shortcuts import redirect


class IndexViewMixin(ListView):
    ordering = ['pk']

    # Add support for custom template tag "table_sort"
    def get_ordering(self):
        if self.request.GET.get('sort_by'):
            self.ordering = self.request.GET.get('sort_by').split("___")
        return self.ordering


class CreateViewMixin(SuccessMessageMixin, CreateView):

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=400)


class UpdateViewMixin(SuccessMessageMixin, UpdateView):

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=400)


class DeleteViewMixin(SuccessMessageMixin, DeleteView):
    failure_message = 'Cannot delete object because it is in use.'
    redirect_url = '/'
    success_url = '/'
    have_dependencies = False

    def post(self, request, *args, **kwargs):
        if not self.have_dependencies:
            try:
                return super().post(request, *args, **kwargs)
            except ProtectedError:
                messages.error(self.request, self.failure_message)
                return redirect(self.redirect_url)
        messages.error(self.request, self.failure_message)
        return redirect(self.redirect_url)
