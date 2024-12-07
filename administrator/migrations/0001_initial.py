# Generated by Django 5.1.3 on 2024-12-07 12:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism_familya', models.CharField(max_length=250)),
                ('telefon', models.CharField(max_length=20)),
                ('fillial', models.CharField(max_length=250)),
                ('eamail', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=120)),
                ('rasm', models.ImageField(upload_to='rasmlar/')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=250)),
                ('dars_vaqti', models.CharField(max_length=250)),
                ('dars_kuni', models.CharField(max_length=250)),
                ('kursi', models.CharField(max_length=250)),
                ('dars_xonasi', models.CharField(choices=[('beginner', 'Beginner'), ('backend', 'Backend'), ('frontend', 'Frontend'), ('grafik dizayn', 'Grafik dizayn'), ('3D dizayn', '3D dizayn')], max_length=250)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
                ('studentlar', models.ManyToManyField(related_name='gruhlar', to='student.student')),
            ],
        ),
    ]