from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View, i18n
from django.utils.translation import gettext as _, activate


class IndexView(View):

    def get(self, request):
        trans = _('Hello World')
        return render(request, 'index.html', context={'data': trans})
