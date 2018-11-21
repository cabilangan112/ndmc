from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post,Course,Department, Author
from django.contrib.auth.models import User, Group
from django.utils.timesince import timesince
 
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )


class pdfdriveserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'