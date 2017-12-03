from django.conf.urls import url, include
from django.contrib import admin
from users import views

urlpatterns = [
    url(r'^/accounts/register/$', views.register, name='register'),
]
