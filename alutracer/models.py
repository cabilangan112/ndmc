from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

CIVIL_STATUS = (
    ('Single', 'Single'),
    ('Married', 'Married')
)

class Question(models.Model):
    user                        = models.ForeignKey(User, on_delete = models.CASCADE)
    question_text               = models.CharField(max_length = 500)
    date_created                = models.DateTimeField(auto_now_add = True)
    date_modified               = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '{}'.format(question_text)

    class Meta:
        ordering = ['-id']

class Choice(models.Model):
    user                        = models.ForeignKey(User, on_delete = models.CASCADE)
    question                    = models.ForeignKey('Question', on_delete = models.CASCADE)
    choices_text                = models.CharField(max_length = 255)
    date_created                = models.DateTimeField(auto_now_add = True)
    date_modified               = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '{}'.format(choices_text)

class Course(models.Model):
    user                        = models.ForeignKey(User, on_delete = models.CASCADE)
    course_code                 = models.CharField(max_length = 255)
    course_description          = models.TextField()
    date_created                = models.DateTimeField(auto_now_add = True)
    date_modified               = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '{}'.format(course_code)

    class Meta:
        ordering = ['-id']

class PersonalInformation(models.Model):
    user                        = models.ForeignKey(User, on_delete = models.CASCADE)
    last_name                   = models.CharField(max_length = 255)
    first_name                  = models.CharField(max_length = 255)
    middle_name                 = models.CharField(max_length = 255)
    gender                      = models.CharField(
                                                    max_length = 6,
                                                    choices = GENDER
                                                )
    date_of_birth               = models.DateTimeField()
    civil_status                = models.CharField(
                                                max_length = 10,
                                                choices = CIVIL_STATUS
                                            )
    age                         = models.IntegerField()
    email                       = models.EmailField()
    address                     = models.TextField()
    country                     = models.TextField()
    social_media_account        = models.CharField(max_length = 255)
    mobile_number               = models.IntegerField()
    course                      = models.ForeignKey('PersonalInformation', on_delete = models.CASCADE)
    date_graduated              = models.DateTimeField()
    date_created                = models.DateTimeField(auto_now_add = True)
    date_modified               = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '{}'.format(self.last_name)

    class Meta:
        ordering = ['-id']