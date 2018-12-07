from django.db import models
from django.conf import settings 
from django.urls import reverse
import uuid

User = settings.AUTH_USER_MODEL

# Create your models here.
class Confirmation(models.Model):
    """ change password confirmation model
    """
    id = models.UUIDField(primary_key=True,
                        default=uuid.uuid4,
                        editable=False)
    url = models.CharField(max_length=500, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.id)

    def save(self, *args, **kwargs):
        self.url = reverse('users:changepass', args={str(self.id)})

        return super(Confirmation, self).save(*args, **kwargs)