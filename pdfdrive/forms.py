from django import forms
from .models import Post,Department,Author, Course
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.forms.widgets import FileInput