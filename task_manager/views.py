from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.utils.translation import gettext as _
from task_manager.forms import LoginForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class IndexView(View):

    def get(self, request):
        user = None
        if request.user.is_authenticated:
            user = request.user
        trans = _('Hello World')
        return render(request, 'index.html', context={'data': trans, 'user': user})


class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )

            if user and user.is_active:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, _('You are logged in'))
                return redirect('index')
        error_message = _('Please enter the correct username and password. '
                          'Both fields can be case sensitive.')
        form = LoginForm()
        return render(request, 'login.html', {'form': form, 'error': error_message})


class LogoutView(View):

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.INFO, _('You are logged out'))
        return redirect('index')


def page_not_found_view(request, *args, **kwargs):
    return render(request, '404.html', status=404)


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
    redirect_url = ''
    is_correct_data = True

    def process(self, request, obj):
        if self.is_correct_data:
            obj.delete()
            messages.add_message(
                self.request,
                messages.SUCCESS,
                self.valid_data_message
            )
            return redirect(self.redirect_url)
        messages.add_message(
            self.request,
            messages.ERROR,
            self.invalid_data_message
        )
        return redirect(self.redirect_url)
