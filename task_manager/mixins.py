from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class LoginRequireMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')
    redirect_field_name = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(
                request,
                messages.ERROR,
                _("You are not authorized! Please log in.")
            )
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class LimitedPermissionsMixin(LoginRequireMixin):
    redirect_url = reverse_lazy('index')
    permission_denied_message = 'You do not have permissions!'
    have_permission = False

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and not self.have_permission:
            messages.add_message(
                request,
                messages.ERROR,
                self.permission_denied_message
            )
            return redirect(self.redirect_url)
        return LoginRequireMixin.dispatch(self, request, *args, **kwargs)
