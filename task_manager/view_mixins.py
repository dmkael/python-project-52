from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect


class CreateFlashedView(CreateView):
    valid_form_message = "Object has been successfully created."

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            self.valid_form_message
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=400)


class UpdateFlashedView(UpdateView):
    valid_form_message = "Object has been successfully updated."

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            self.valid_form_message
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=400)


class DeleteFlashedView(DeleteView):
    valid_data_message = 'Object has been deleted successfully.'
    invalid_data_message = 'Cannot delete object because it is in use.'
    redirect_url = '/'
    success_url = '/'
    is_correct_data = True

    def post(self, request, *args, **kwargs):
        if self.is_correct_data:
            messages.add_message(
                self.request,
                messages.SUCCESS,
                self.valid_data_message
            )
            return super().post(request, *args, **kwargs)
        messages.add_message(
            self.request,
            messages.ERROR,
            self.invalid_data_message
        )
        return redirect(self.redirect_url)
