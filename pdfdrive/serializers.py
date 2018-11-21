from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post
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