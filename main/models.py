from django.db import models


class Specialties(models.Model):
    title = models.CharField(max_length=255)
    speciality = models.ForeignKey('SpecialtiesIds', on_delete=models.PROTECT, verbose_name='Специальность')
    about = models.TextField()
    image_preview_url = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Admissions(models.Model):
    speciality = models.ForeignKey('SpecialtiesIds', on_delete=models.PROTECT, verbose_name='Специальность')
    fio = models.CharField(max_length=32, verbose_name='Ф.И.О.')
    birthday = models.DateField(verbose_name='День рождения')
    education_status = models.CharField(max_length=16, verbose_name='Ваше текущее образование')
    phone = models.CharField(max_length=32, verbose_name='Номер телефона')
    email = models.CharField(max_length=32, verbose_name='Электронная почта', null=True)


class SpecialtiesIds(models.Model):
    name = models.CharField(max_length=16, verbose_name='Специальность')
