from django.urls import path
from . import views

app_name='pdfdrive'
urlpatterns = [
    path('', views.PostView.as_view(), name='post'),
    path('<title>/', views.PostDetailView.as_view(), name='detail'),
#    path('post/', views.UploadPost.as_view(), name='post')
]