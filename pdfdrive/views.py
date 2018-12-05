from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.views.generic import (ListView,DetailView,CreateView,UpdateView, View)
from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)
from django.contrib.auth import get_user_model
from .models import Post,Department,Author, Course
from .forms import PostForm,DepartmentForm,CourseForm,AuthorForm

class PostView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.all()
        context = {'post':post,}
        return render(request, "pdfdrive/pdf_list.html", context)

class PostDetailView(View):
    def get(self, request, title, *args, **kwargs):
        post = get_object_or_404(Post, title=title)
        context = {'post':post,}
        return render(request, "pdfdrive/pdf_detail.html", context)

class UploadPost(View):
    def get(self, request):
        post_list = Post.objects.all()
        return render(self.request, 'pdfdrive/upload.html', {'post': post_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': post.file.name, 'url': post.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)