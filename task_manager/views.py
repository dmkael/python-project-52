from django.shortcuts import render
from django.views import View
from django.conf.urls.static import static


class IndexView(View):

    def get(self, request):
        data = 'Hello World'
        return render(request, 'index.html', context={'data': data})
