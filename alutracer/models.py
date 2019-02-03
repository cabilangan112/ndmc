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
    ('Married', 'Married'),
    ('Separated', 'Separated'),
    ('Widowed', 'Widowed')
)

class Index(models.Model):
    user                                = models.ForeignKey(User, on_delete = models.CASCADE)
    cover_photo                         = models.ImageField(upload_to = 'media')
    title                               = models.CharField(max_length = 255)
    description                         = models.TextField()
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

class Parallax(models.Model):
    user                                = models.ForeignKey(User, on_delete = models.CASCADE)
    parallax_1                          = models.ImageField(upload_to='media')
    parallax_1_heading                  = models.CharField(max_length=255)
    parallax_1_content                  = models.TextField()
    parallax_2                          = models.ImageField(upload_to='media')
    parallax_2_heading                  = models.CharField(max_length=255)
    parallax_2_content                  = models.TextField()
    date_created                        = models.DateTimeField(auto_now_add = True)
    date_modified                       = models.DateTimeField(auto_now = True)
    slug                                = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.parallax_1_heading)

    @property
    def slug_title(self):
        return '{}'.format(self.parallax_1_heading)

    class Meta:
        ordering = ['-id']

class Thumbnail(models.Model):
    user                                = models.ForeignKey(User, on_delete = models.CASCADE)
    thumbnail                           = models.ImageField(upload_to='media')
    date_created                        = models.DateTimeField(auto_now_add = True)
    date_modified                       = models.DateTimeField(auto_now = True)
    slug                                = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.user)

    @property
    def slug_title(self):
        return '{}'.format(self.user)

    class Meta:
        ordering = ['-id']

class Course(models.Model):
    user                                = models.ForeignKey(User, on_delete = models.CASCADE)
    course_code                         = models.CharField(max_length = 255)
    course_description                  = models.TextField()
    date_created                        = models.DateTimeField(auto_now_add = True)
    date_modified                       = models.DateTimeField(auto_now = True)
    slug                                = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.course_code, self.course_description)

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
    date_of_birth                       = models.DateField()
    civil_status                        = models.CharField(
                                                        max_length = 10,
                                                        choices = CIVIL_STATUS
                                                    )
    age                                 = models.IntegerField()
    email                               = models.EmailField()
    mobile_number                       = models.CharField(max_length = 20)
    a_street_adress                     = models.TextField()
    a_address_line_2                    = models.TextField()
    a_city                              = models.CharField(max_length = 255)
    a_state_province_region             = models.TextField()
    a_zip_code                          = models.CharField(max_length = 255)
    a_country                           = models.CharField(max_length = 255)

    b_street_adress                     = models.TextField()
    b_address_line_2                    = models.TextField()
    b_city                              = models.CharField(max_length = 255)
    b_state_province_region             = models.TextField()
    b_zip_code                          = models.CharField(max_length = 255)
    b_country                           = models.CharField(max_length = 255)

    course                              = models.ForeignKey('Course', on_delete = models.CASCADE)
    date_graduated                      = models.DateTimeField()
    
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

pre_save.connect(rl_pre_save_receiver, sender=Index)
pre_save.connect(rl_pre_save_receiver, sender=Thumbnail)
pre_save.connect(rl_pre_save_receiver, sender=Parallax)
pre_save.connect(rl_pre_save_receiver, sender=Course)
pre_save.connect(rl_pre_save_receiver, sender=PersonalInformation)