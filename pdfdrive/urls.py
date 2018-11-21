from django.urls import path
 
app_name='pdfdrive'
from .views import pdflistAPI
 

pdf_list = pdflistAPI.as_view({
	'get': 'list',
	'post':'create'
})
urlpatterns = [
	path('list', pdf_list, name='list'),
	]