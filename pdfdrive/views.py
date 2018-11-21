from django.shortcuts import render
from .models import Post,Department,Author, Course
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .serializers import pdfdriveserializer,CourseSerializer,DepartmentSerializer,AuthorSerializer
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

class CourseAPI(ViewSet):

    def list(self ,request):
        queryset = Course.objects.all()
        serializer_context = {'request': request,}
        serializer = CourseSerializer(queryset, many=True, context=serializer_context)
        return Response(serializer.data)

    def create(self, *args, **kwargs):
         
        serializer = CourseSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)


class DepartmentAPI(ViewSet):

    def list(self ,request):
        queryset = Department.objects.all()
        serializer_context = {'request': request,}
        serializer = DepartmentSerializer(queryset, many=True, context=serializer_context)
        return Response(serializer.data)

    def create(self, *args, **kwargs):
         
        serializer = DepartmentSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)


class AuthorAPI(ViewSet):

    def list(self ,request):
        queryset = Author.objects.all()
        serializer_context = {'request': request,}
        serializer = AuthorSerializer(queryset, many=True, context=serializer_context)
        return Response(serializer.data)

    def create(self, *args, **kwargs):
         
        serializer = AuthorSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)

