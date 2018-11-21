from django.contrib import admin
from .models import Course, Choice, PersonalInformation, Question

class ChoceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['question_text']}),
    ]
    inline = [ChoceInline]
    list_display = ('question_text', 'date_created', 'date_modified')
    search_fields = ['question_text']
    list_filter = ['date_created']

admin.site.register(Course)
admin.site.register(Choice)
admin.site.register(PersonalInformation)
admin.site.register(Question, QuestionAdmin)

# Register your models here.
