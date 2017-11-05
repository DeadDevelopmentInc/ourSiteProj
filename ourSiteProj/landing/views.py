from django.shortcuts import render

# Create your views here.

def index(request):

	return render(request, 'index.html', locals())

def contacts(request):

	return render(request, 'contacts.html', locals())

def register(request):

	return render(request, 'register.html', locals())

def press(request):

	return render(request, 'press.html', locals())

def researches(request):

	return render(request, 'researches.html', locals())

def services(request):

	return render(request, 'services.html', locals())
