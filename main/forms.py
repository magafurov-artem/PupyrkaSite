from django import forms
from .models import *


# class SendAdmissions(forms.Form):
#     # speciality = forms.ModelChoiceField(queryset=Specialties.objects.values_list('title', flat=True),
#     #                                     empty_label=None, label='Специальность', to_field_name='about')
#     speciality = forms.ModelChoiceField(queryset=Specialties.objects.all(),
#                                         empty_label=None, label='Специальность', to_field_name='id')
#     fio = forms.CharField(max_length=32, label='Ф.И.О.')
#     birthday = forms.CharField(max_length=32, label='День рождения')
#     phone = forms.CharField(max_length=32, label='Номер телефона')


# class MyModelChoiceField(forms.ModelChoiceField):
#     def label_from_instance(self, obj):
#         return obj.name


class SendAdmissions(forms.ModelForm):
    # speciality_id = forms.ModelChoiceField(queryset=SpecialtiesIds.objects.all(),
    #                                        empty_label=None, label='Выбор специальности', to_field_name='id')

    class Meta:
        model = Admissions
        fields = ['speciality', 'fio', 'birthday', 'education_status', 'phone', 'email']
