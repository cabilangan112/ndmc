from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings
from .validators import validate_file_extention
from django.urls import reverse
 

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

