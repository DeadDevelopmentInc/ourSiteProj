from django.conf.urls import url, include
from django.contrib import admin
from landing import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
]
