from django.urls import path
 
app_name='pdfdrive'
from .views import PDFListAPI,AuthorAPI,DepartmentAPI,CourseAPI

pdf = PDFListAPI.as_view({
	'get': 'list',
	'post':'create',
 
})

pdf_detail = PDFListAPI.as_view({
	'get':'put',
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
	path('pdf/', pdf, name='pdflist'),
	path('course/', course, name='courselist'),
	path('department/', department, name='deplist'),
	path('author/', author, name='authorlist'),
	#details
 	path('pdf/<int:pk>/', pdf_detail, name='pdfdetail'),
 	path('course/<int:pk>/', course_detail, name='coursedetail'),
	path('department/<int:pk>/', department_detail, name='depdetail'),
	path('author/<int:pk>/', author_detail, name='authordetail'),
	#edit
 
	]