from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views
# app_name = 'image'
urlpatterns = [
    path('', views.main2, name='index'),
    #path('main', views.main2),
    path('upload', views.upload),
    #path('passes', views.upload2)
    #path('upload_success', views.upload_success),
    # path('upload/', views.upload, name='upload'),
]
