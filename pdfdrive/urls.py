from django.urls import path
 
app_name='pdfdrive'
from .views import pdflistAPI,AuthorAPI,DepartmentAPI,CourseAPI
 

pdf = pdflistAPI.as_view({
	'get': 'list',
	'post':'create'
})

course = CourseAPI.as_view({
	'get': 'list',
	'post':'create'
})

department = DepartmentAPI.as_view({
	'get': 'list',
	'post':'create'
})

author = AuthorAPI.as_view({
	'get': 'list',
	'post':'create'
})

urlpatterns = [
	path('pdflist', pdf, name='pdflist'),
	path('course', course, name='courselist'),
	path('departmentlist', department, name='deplist'),
	path('authorlist', author, name='authorlist'),
	]