from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
# Create your views here.


def home(request):
    return render(request, 'solapp/home.html')


def about(request):
    return render(request, 'solapp/about.html')


def news(request):
    return render(request, 'solapp/news.html')


def gallery(request):
    return render(request, 'solapp/gallery.html')


def contactus(request):
    return render(request, 'solapp/contact.html')