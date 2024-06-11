from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect


class CreateFlashedView(SuccessMessageMixin, CreateView):

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=400)


class UpdateFlashedView(SuccessMessageMixin, UpdateView):

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=400)


class DeleteFlashedView(SuccessMessageMixin, DeleteView):
    failure_message = 'Cannot delete object because it is in use.'
    redirect_url = '/'
    success_url = '/'
    have_dependencies = False

    def post(self, request, *args, **kwargs):
        if not self.have_dependencies:
            return super().post(request, *args, **kwargs)
        messages.add_message(
            self.request,
            messages.ERROR,
            self.failure_message
        )
        return redirect(self.redirect_url)
