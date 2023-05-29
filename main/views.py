from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from .models import Specialties
# Create your views here.


def index(request: WSGIRequest):
    container = {'specialties': Specialties.objects.all()}
    return render(request, 'main/index.html', container)


def about(request: WSGIRequest):
    return render(request, 'main/about.html')


def contact(request: WSGIRequest):
    return render(request, 'main/contact.html')


def applicants(request: WSGIRequest):
    return render(request, 'main/applicants.html')


def students(request: WSGIRequest):
    return render(request, 'main/students.html')
