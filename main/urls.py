from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('our_contact', views.contact, name='contact'),
    path('applicants', views.applicants, name='applicants'),
    path('students', views.students, name='students')
]