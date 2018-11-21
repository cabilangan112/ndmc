from django.urls import path

app_name='alutracer'

from .views import CourseAPIView, ChoiceAPIView, PersonalInformationAPIView, QuestionAPIView

course_list = CourseAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })

course_detail = CourseAPIView.as_view({
        'get': 'retrieve',
        # 'post': 'edit'
    })

choice_list = ChoiceAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })

choice_detail = ChoiceAPIView.as_view({
        'get': 'retrieve',
        # 'post': 'create'
    })

personal_information_list = PersonalInformationAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })

personal_information_detail = PersonalInformationAPIView.as_view({
        'get': 'retrieve',
        # 'post': 'create'
    })

question_list = QuestionAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })

question_detail = QuestionAPIView.as_view({
        'get': 'retrieve',
        # 'post': 'create'
    })

urlpatterns = [
    path('course', course_list, name='course-list'),
    path('choice', choice_list, name='choice-list'),
    path('personal-information', personal_information_list, name='personal-information-list'),
    path('question', question_list, name='question-list'),
    path('course/<str:pk>', course_detail, name='course-detail'),
    path('choice/<str:pk>', choice_detail, name='choice-detail'),
    path('personal-information/<str:pk>', personal_information_detail, name='personal-information-detail'),
    path('question/<str:pk>', question_detail, name='question-detail')
]
