from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
    url(r'register/', views.register, name='register'),
    url(r'user_info/', views.user_info, name='user_info'),
    url(r'user_info_edit/', views.myself_edit, name='user_info_edit'),
    url(r'upload_image/', views.my_image, name='upload_image')
]
