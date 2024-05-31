from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.utils.translation import gettext as _
from task_manager.forms import LoginForm


class IndexView(View):

    def get(self, request):
        user = None
        if request.user.is_authenticated:
            user = request.user
        trans = _('Hello World')
        return render(request, 'index.html', context={'data': trans, 'user': user})


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
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
                return redirect('index')
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


class LogoutView(View):

    def post(self, request):
        logout(request)
        return redirect('index')
