from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View
from django.utils.translation import gettext as _
from django.contrib.auth.views import LoginView


class IndexView(View):

    def get(self, request):
        user = None
        if request.user.is_authenticated:
            user = request.user
        trans = _('Hello World')
        return render(request, 'index.html', context={'data': trans, 'user': user})


class TaskManagerLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('You are logged in')
        )
        return super().form_valid(form)


class TaskManagerLogoutView(View):

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.INFO, _('You are logged out'))
        return redirect('index')


def page_not_found_view(request, *args, **kwargs):
    return render(request, '404.html', status=404)
