# Generated by Django 4.1.7 on 2023-06-04 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_specialtiestags_specialtiesids_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admissions',
            name='speciality',
        ),
        migrations.AddField(
            model_name='admissions',
            name='speciality_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='main.specialtiesids', verbose_name='Специальность'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='admissions',
            name='email',
            field=models.CharField(max_length=32, null=True, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='specialties',
            name='speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.specialtiesids', verbose_name='Специальность'),
        ),
    ]