from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import Course, Choice, PersonalInformation, Question
from .serializers import CourseSerializer, ChoiceSerializer, PersonalInformationSerializer, QuestionSerializer

# Create your views here.

class CourseAPIView(ViewSet):
    def list(self, request):
        queryset = Course.objects.all()
        serializer_context = {'request' : request}
        serializer = CourseSerializer(queryset, many = True, context = serializer_context)
        return Response(serializer.data)

    def create(self, *args, **kwargs):
        serializer = CourseSerializer(data = self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = 201)
        return Response(serializer.errors, status = 400)

class ChoiceAPIView(ViewSet):
    def list(self, request):
        queryset = Choice.objects.all()
        serializer_context = {'request' : request}
        serializer = ChoiceSerializer(queryset, many = True, context = serializer_context)
        return Response(serializer.data)

    def create(self, *args, **kwargs):
        serializer = ChoiceSerializer(data = self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = 201)
        return Response(serializer.errors, status = 400)

class QuestionAPIView(ViewSet):
    def list(self, request):
        queryset = Question.objects.all()
        serializer_context = {'request' : request}
        serializer = QuestionSerializer(queryset, many = True, context = serializer_context)
        return Response(serializer.data)

    def create(self, *args, **kwargs):
        serializer = QuestionSerializer(data = self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = 201)
        return Response(serializer.errors, status = 400)

class PersonalInformationAPIView(ViewSet):
    def list(self, request):
        queryset = PersonalInformation.objects.all()
        serializer_context = {'request' : request}
        serializer = PersonalInformationSerializer(queryset, many = True, context = serializer_context)
        return Response(serializer.data)

    def create(self, *args, **kwargs):
        serializer = PersonalInformationSerializer(data = self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = 201)
        return Response(serializer.errors, status = 400)