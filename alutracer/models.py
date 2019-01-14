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
    address                             = models.TextField()
    country                             = models.TextField()
    social_media_account                = models.CharField(max_length = 255)
    mobile_number                       = models.CharField(max_length = 20)
    course                              = models.ForeignKey('Course', on_delete = models.CASCADE)
    date_graduated                      = models.DateTimeField()
    organization_or_employer            = models.CharField(max_length = 255)
    address_organization_or_employer    = models.CharField(max_length = 255)
    type_of_organization                = models.CharField(max_length = 20)
    related_job                         = models.CharField(max_length = 3)
    number_year_company                 = models.CharField(max_length = 3)
    place_of_work                       = models.CharField(max_length = 6)
    finish_graduate_degree              = models.CharField(max_length = 3)
    reason_staying_job                  = models.TextField()
    designation                         = models.CharField(max_length = 255)
    department_division                 = models.CharField(max_length = 255)
    job_status                          = models.CharField(max_length = 11)
    monthly_range_income                = models.CharField(max_length = 255)
    persuing_degree_ndmc                = models.CharField(max_length = 3)
    obtaining_degree_ndmc               = models.TextField()
    advertisement_media                 = models.TextField()
    nature_of_employment                = models.CharField(max_length=500)
    number_of_years                     = models.CharField(max_length = 3)
    monthly_income                      = models.CharField(max_length = 255)
    case_of_unemployed                  = models.TextField()
    persuing_futher_studies             = models.TextField()
    not_persuing_futher_studies         = models.TextField()
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