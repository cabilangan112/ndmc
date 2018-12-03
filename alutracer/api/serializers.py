from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Course, Choice, PersonalInformation, Question

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'user',
            'course_code', 
            'course_description',
            'date_created',
            'date_modified'
        ]

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = [
            'id',
            'user',
            'question',
            'choices_text',
            'date_created',
            'date_modified'
        ]

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id',
            'user',
            'question_text',
            'date_created',
            'date_modified'
        ]

class PersonalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInformation
        fields = [
            'id',
            'user',
            'last_name',
            'first_name',
            'middle_name',
            'gender',
            'date_of_birth',
            'civil_status',
            'age',
            'email',
            'address',
            'country',
            'social_media_account',
            'mobile_number',
            'date_graduated',
            'organization_or_employer',
            'address_organization_or_employer',
            'date_created',
            'date_modified'
        ]