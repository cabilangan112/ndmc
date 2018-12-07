from django.shortcuts import render
from django.views import View
from .models import Index, Thumbnail, Parallax
from pdfdrive.models import Post
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        index = Index.objects.all()
        parallax = Parallax.objects.all()[:1]
        pdf_list = Post.objects.all()[:3]
        thumbnail = Thumbnail.objects.all()[:3]
        context = {
            'index': index,
            'pdf_list': pdf_list,
            'parallax': parallax,
            'thumbnail': thumbnail
        }
        return render(request, 'home.html', context)