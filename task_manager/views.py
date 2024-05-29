from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext as _
from task_manager.forms import LoginForm


class IndexView(View):

    def get(self, request):
        trans = _('Hello World')
        return render(request, 'index.html', context={'data': trans})


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
