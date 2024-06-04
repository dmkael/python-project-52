from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class AuthorizedOnlyMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(
                request,
                messages.ERROR,
                _('You are not logged in.')
            )
            return redirect('login')

        if request.user.id == kwargs.get('pk'):
            return super().dispatch(request, *args, **kwargs)

        messages.add_message(
            request,
            messages.ERROR,
            _("You do not have permission to perform this action.")
        )
        return redirect('users')
