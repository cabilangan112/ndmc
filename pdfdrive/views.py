from django.shortcuts import render
from .models import Post,Department,Author, Course
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .serializers import pdfdriveserializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

class pdflistAPI(ViewSet):

    def list(self ,request):
        queryset = Post.objects.all()
        serializer_context = {'request': request,}
        serializer = pdfdriveserializer(queryset, many=True, context=serializer_context)
        return Response(serializer.data)

    def create(self, *args, **kwargs):
         
        serializer = pdfdriveserializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)