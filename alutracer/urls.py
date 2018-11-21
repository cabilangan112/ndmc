from django.urls import path

app_name='alutracer'

from .views import CourseAPIView, ChoiceAPIView, PersonalInformationAPIView, QuestionAPIView

CourseAPI = CourseAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })

ChoiceAPI = ChoiceAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })

PersonalInformationAPI = PersonalInformationAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })

QuestionAPI = QuestionAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })

urlpatterns = [
    path('course', CourseAPI, name='course-list'),
    path('choice', ChoiceAPI, name='choice-list'),
    path('personal-information', PersonalInformationAPI, name='personal-information-list'),
    path('question', QuestionAPI, name='question-list'),
]
