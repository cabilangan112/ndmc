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
    date_uplaod = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id',
                  'title', 
                  'description',
                  'author',
                  'author_name',
                  'file',
                  'date_uplaod',
                  'timesince',
                  ]

    def get_author_name(self,instance):
       return instance.author.lastname

    def get_date_uplaod(self, instance):
        return instance.date_uploaded.strftime("%b %d, %Y | at %I:%M %p")

    def get_timesince(self, instance):
        return timesince(instance.modified) + " ago"   

class CourseSerializer(serializers.ModelSerializer):
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = ['id',
                  'course_code',
                  'course_description',
                  'date_display',
                  'timesince'
                  ]

    def get_date_display(self, instance):
        return instance.date_created.strftime("%b %d, %Y | at %I:%M %p")

    def get_timesince(self, instance):
        return timesince(instance.date_modified) + " ago"

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    department_code = serializers.SerializerMethodField()
    course_code = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['id',
                  'lastname',
                  'firstname',
                  'middlename',
                  'department',
                  'department_code',
                  'course',
                  'course_code',
                  'year',
                  ]

    def get_department_code(self,instance):
        return instance.department.department_code

    def get_course_code(self,instance):
        return instance.course.course_code