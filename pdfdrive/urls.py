from django.urls import path
from .views import PDFListAPI,AuthorAPI,DepartmentAPI,CourseAPI

app_name='pdfdrive'

pdf = PDFListAPI.as_view({
    'get': 'list',
    'post':'create'
})

pdf_detail = PDFListAPI.as_view({
	'get':'post',
	'get':'retrieve'
})

course = CourseAPI.as_view({
    'get': 'list',
    'post':'create'
})

course_detail = CourseAPI.as_view({
    'get':'details',
    'post':'edit'
})


department = DepartmentAPI.as_view({
    'get': 'list',
    'post':'create'
})

department_detail = DepartmentAPI.as_view({
    'get':'details',
    'post':'edit'
})

author = AuthorAPI.as_view({
    'get':'list',
    'post':'create'
})

author_detail = AuthorAPI.as_view({
    'get':'details',
    'post':'edit'
})

urlpatterns = [
    path('pdf/', pdf, name='pdf-list'),
    path('course/', course, name='course-list'),
    path('department/', department, name='dep-list'),
    path('author/', author, name='author-list'),
    #details
    path('pdf/<int:pk>/', pdf_detail, name='pdf-detail'),
    path('course/<int:pk>/', course_detail, name='course-detail'),
    path('department/<int:pk>/', department_detail, name='dep-detail'),
    path('author/<int:pk>/', author_detail, name='author-detail')
    ]