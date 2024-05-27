from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext as _, activate


class IndexView(View):

    def get(self, request):
        activate('es')
        trans = _('Hello World')
        return render(request, 'index.html', context={'data': trans})
