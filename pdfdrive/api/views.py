from django.shortcuts import render
from .models import Post,Department,Author, Course
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .serializers import pdfdriveserializer,PdfDriveEditSerializer,CourseSerializer,DepartmentSerializer,AuthorSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet 

class PDFListAPI(ViewSet):

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


    def get_author(self, *args, **kwargs):
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializers.data)

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def edit(self, request,   format=None):
        serializer = pdfdriveserializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save()
            for author in request.data.get('authors'):
                a = Author.objects.get(id=author)
                post.authors.add(a)
                import pdb; pdb.set_trace()
            return Response(serializer.data)
        return Response(serializer.errors )

    def put(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer_context = {'request': request,}
        serializer = pdfdriveserializer(post, context=serializer_context)
        return Response(serializer.data)


    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

 
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

