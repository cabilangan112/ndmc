from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings

from .utils import unique_slug_generator

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

class Home(models.Model):
    user                                = models.ForeignKey(User, on_delete = models.CASCADE)
    cover_photo                         = models.ImageField(upload_to = 'media')
    title                               = models.CharField(max_length = 255)
    description                         = models.TextField()
    content_heading                     = models.CharField(max_length=255)
    content_description                 = models.TextField()
    parallax_1                          = models.ImageField(upload_to='media')
    parallax_1_heading_content          = models.CharField(max_length=255)
    parallax_1_content                  = models.TextField()
    parallax_2                          = models.ImageField(upload_to='media')
    parallax_2_heading_content          = models.CharField(max_length=255)
    parallax_2_content                  = models.TextField()
    thumbnail                           = models.ImageField(upload_to='media')
    footer_heading                      = models.CharField(max_length=255)
    footer_content                      = models.TextField()
    date_created                        = models.DateTimeField(auto_now_add = True)
    date_modified                       = models.DateTimeField(auto_now = True)
    slug                                = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.title)

    @property
    def slug_title(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['-id']

class Question(models.Model):
    user                                = models.ForeignKey(User, on_delete = models.CASCADE)
    question_text                       = models.CharField(max_length = 500)
    date_created                        = models.DateTimeField(auto_now_add = True)
    date_modified                       = models.DateTimeField(auto_now = True)
    slug                                = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.question_text)

    @property
    def slug_title(self):
        return '{}'.format(self.question_text)

    class Meta:
        ordering = ['-id']

class Choice(models.Model):
    user                                = models.ForeignKey(User, on_delete = models.CASCADE)
    question                            = models.ForeignKey('Question', on_delete = models.CASCADE)
    choices_text                        = models.CharField(max_length = 255)
    date_created                        = models.DateTimeField(auto_now_add = True)
    date_modified                       = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return '{}'.format(self.choices_text)

class Course(models.Model):
    user                                = models.ForeignKey(User, on_delete = models.CASCADE)
    course_code                         = models.CharField(max_length = 255)
    course_description                  = models.TextField()
    date_created                        = models.DateTimeField(auto_now_add = True)
    date_modified                       = models.DateTimeField(auto_now = True)
    slug                                = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.course_code)

    @property
    def slug_title(self):
        return '{}'.format(self.course_code)

    class Meta:
        ordering = ['-id']

class PersonalInformation(models.Model):
    user                                = models.ForeignKey(User, on_delete = models.CASCADE)
    last_name                           = models.CharField(max_length = 255)
    first_name                          = models.CharField(max_length = 255)
    middle_name                         = models.CharField(max_length = 255)
    gender                              = models.CharField(
                                                            max_length = 6,
                                                            choices = GENDER
                                                        )
    date_of_birth                       = models.DateTimeField()
    civil_status                        = models.CharField(
                                                        max_length = 10,
                                                        choices = CIVIL_STATUS
                                                    )
    age                                 = models.IntegerField()
    email                               = models.EmailField()
    address                             = models.TextField()
    country                             = models.TextField()
    social_media_account                = models.CharField(max_length = 255)
    mobile_number                       = models.IntegerField()
    course                              = models.ForeignKey('PersonalInformation', on_delete = models.CASCADE)
    date_graduated                      = models.DateTimeField()
    organization_or_employer            = models.CharField(max_length = 255)
    address_organization_or_employer    = models.CharField(max_length = 255)
    date_created                        = models.DateTimeField(auto_now_add = True)
    date_modified                       = models.DateTimeField(auto_now = True)
    slug                                = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{}, {} {}'.format(
                        self.last_name,
                        self.first_name,
                        self.middle_name,
                        )

    @property
    def slug_title(self):
        return '{}'.format(self.last_name)

    class Meta:
        ordering = ['-id']

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Home)
pre_save.connect(rl_pre_save_receiver, sender=Question)
pre_save.connect(rl_pre_save_receiver, sender=Course)
pre_save.connect(rl_pre_save_receiver, sender=PersonalInformation)