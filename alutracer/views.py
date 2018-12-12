from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (
        Course,
        Index,
        Thumbnail,
        Parallax,
        PersonalInformation
    )
from pdfdrive.models import Post
from .forms import PersonalInformationForm
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

class PersonalInfoDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        personal_info_detail = get_object_or_404(PersonalInformation, slug=slug)
        context = {
            'personal_info_detail':personal_info_detail
        }
        return render(request, 'alutracer/alu-detail.html', context)

class PersonalInfoCreateView(View):
    form_class = PersonalInformationForm
    initial = {'key':'value'}
    template_name = 'alutracer/alu-form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('personal-info-detail', slug=post.slug)
        else:
            form = PersonalInformationForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)