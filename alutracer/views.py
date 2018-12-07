from django.shortcuts import render
from django.views import View
from .models import Index
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        index = Index.objects.all()[:3]
        context = {
            'index': index,
        }
        return render(request, 'home.html', context)