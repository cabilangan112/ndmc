from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings
from .validators import validate_file_extention
from django.urls import reverse
User = settings.AUTH_USER_MODEL

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class PathAndRename(object):

    def __init__(self,sub_path):
        self.path = sub_path

    def __call__(self,instance, filename):
        ext = filename.split('.')[-1]

        if instance.pk:
            filename = '{}.{}'.format(instance.pk,ext)
        else:
            filename = '{}.{}'.format(instance.pk,ext)
        return os.path.join(self.path, filename)
path_and_rename = PathAndRename("media/file/")

YEAR = (
    ('1st', '1st'),
    ('2nd', '2nd'),
    ('3rd', '3rd'),
    ('4rt', '4rt'),
)

class Course(models.Model):
    course_code        = models.CharField(max_length=100)
    course_description = models.CharField(max_length=100) 
    date_created       = models.DateTimeField(auto_now_add=True)
    date_modified      = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.course_code)
ss
    class Meta:
        ordering = ['-date_created']


class Department(models.Model):
    department_code        = models.CharField(max_length=100)
    department_description = models.CharField(max_length=100) 
    date_created           = models.DateTimeField(auto_now_add=True)
    date_modified          = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.department_code)

    class Meta:
        ordering = ['-date_created']

class Author(models.Model):
    lastname           = models.CharField(max_length=100)
    firstname          = models.CharField(max_length=100)
    middlename         = models.CharField(max_length=100)
    department         = models.ForeignKey(Department, null=True,on_delete=models.CASCADE)
    course             = models.ForeignKey(Course, null=True,on_delete=models.CASCADE)
    year               = models.CharField(max_length=6, choices=YEAR, blank=True, default=True)
 
    def __str__(self):
        return '{}'.format(self.lastname,self.firstname)

    class Meta:
        ordering = ['-id']

class Post(models.Model):
    title          = models.CharField(max_length=100)
    description    = models.TextField(null=True, blank=True)
    author         = models.ForeignKey(Author, null=True,on_delete=models.CASCADE)
    file           = models.FileField(upload_to="pdf", null=True)
    date_uploaded  = models.DateTimeField(auto_now_add=True)
    modified       = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['-date_uploaded']

