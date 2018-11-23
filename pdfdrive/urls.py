from django.urls import path
 
app_name='pdfdrive'
from .views import PDFListAPI,AuthorAPI,DepartmentAPI,CourseAPI
 

pdf = PDFListAPI.as_view({
	'get': 'list',
	'post':'create',
 
})

pdf_detail = PDFListAPI.as_view({
	'get':'put',
	'post':'edit'
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
	path('pdflist', pdf, name='pdflist'),
	path('courselist', course, name='courselist'),
	path('departmentlist', department, name='deplist'),
	path('authorlist', author, name='authorlist'),
	#details
 	path('pdfdetail', pdf_detail, name='pdfdetail'),
 	path('coursedetail', course_detail, name='coursedetail'),
	path('departmentdetail', department_detail, name='depdetail'),
	path('authordetail', author_detail, name='authordetail'),
	]