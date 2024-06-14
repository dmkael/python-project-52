from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin
from django.views.generic import ListView
from django.contrib import messages
from django.shortcuts import redirect


class IndexViewMixin(ListView, ContextMixin):
    paginate_by = None
    pass


class CreateViewMixin(SuccessMessageMixin, CreateView, ContextMixin):

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=400)


class UpdateViewMixin(SuccessMessageMixin, UpdateView, ContextMixin):

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=400)


class DeleteViewMixin(SuccessMessageMixin, DeleteView, ContextMixin):
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
