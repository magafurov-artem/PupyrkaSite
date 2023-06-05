from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from .models import Specialties
from .forms import SendAdmissions
from loguru import logger


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


def admissions(request: WSGIRequest):
    if request.method == 'POST':
        form = SendAdmissions(request.POST)
        logger.debug(form.is_valid())
        print(form.cleaned_data)
        # if form.is_valid():
        #     temp = form.save(commit=False)
        #     admissions.speciality_id = form.cleaned_data['speciality']
        #     print(temp.cleaned_data)
        form.save()
    else:
        form = SendAdmissions()
    return render(request, 'main/admissions.html', {'form': form})
