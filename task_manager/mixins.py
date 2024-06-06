from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
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
