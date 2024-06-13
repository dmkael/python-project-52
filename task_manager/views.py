from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.views import LoginView


class IndexView(TemplateView):
    template_name = 'index.html'


class TaskManagerLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = _('You are logged in.')


class TaskManagerLogoutView(View):

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, _('You are logged out'))
        return redirect('index')


def page_not_found_view(request, *args, **kwargs):
    return render(request, '404.html', status=404)
