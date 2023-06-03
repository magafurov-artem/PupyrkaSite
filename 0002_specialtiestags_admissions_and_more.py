# Generated by Django 4.1.7 on 2023-06-03 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialtiesTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='Специальность')),
            ],
        ),
        migrations.CreateModel(
            name='Admissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=32, verbose_name='Ф.И.О.')),
                ('birthday', models.DateField(verbose_name='День рождения')),
                ('education_status', models.CharField(max_length=16, verbose_name='Ваше текущее образование')),
                ('phone', models.CharField(max_length=32, verbose_name='Номер телефона')),
                ('email', models.CharField(max_length=32, verbose_name='Электронная почта')),
                ('speciality_tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.specialtiestags')),
            ],
        ),
        migrations.AddField(
            model_name='specialties',
            name='speciality_tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='main.specialtiestags'),
            preserve_default=False,
        ),
    ]
