from django.conf.urls import url, include
from django.contrib import admin
from landing import views

urlpatterns = [
	url(r'^contacts', views.contacts, name='contacts'),
	url(r'^press', views.press, name='press'),
	url(r'^researches', views.researches, name='researches'),
	url(r'^services', views.services, name='services'),
	url(r'^', views.index, name='index'),
]
