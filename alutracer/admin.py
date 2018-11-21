from django.contrib import admin
from .models import Question,Course, Choice,PersonalInformation

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Course)
admin.site.register(PersonalInformation)

# Register your models here.
