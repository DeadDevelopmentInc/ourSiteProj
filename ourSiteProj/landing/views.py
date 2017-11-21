from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import auth




# Create your views here.

def index(request):

	return render(request, 'index.html',{'username': auth.get_user(request).username})

def contacts(request):

	return render(request, 'contacts.html', locals())

def press(request):

	return render(request, 'press.html', locals())

def researches(request):

	return render(request, 'researches.html', locals())

def services(request):

	return render(request, 'services.html', locals())

def register(request):

    return render(request, 'register.html', locals())
