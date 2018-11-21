from django.shortcuts import render
from .models import Post,Department,Author, Course
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

class repoAPI(ViewSet):
    def list(self ,request):
        queryset = Post.objects.all()
        serializer_context = {'request': request,}
        serializer = pdfdriveserializer(queryset, many=True, context=serializer_context)
        return Response(serializer.data)