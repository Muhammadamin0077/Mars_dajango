from django.db import models
from teacher.models import Teacher
from student.models import Student

# Create your models here.

class Administrator(models.Model):
      ism_familya = models.CharField(max_length=250)
      telefon = models.CharField(max_length=20)
      fillial = models.CharField(max_length=250)
      eamail = models.EmailField()
      username = models.CharField(max_length=120)
      rasm = models.ImageField(upload_to='rasmlar/') 

      def __str__(self):
         return self.ism_familya
      


KURSLAR = [
     ('beginner', 'Beginner'),
     ('backend', 'Backend'),
     ('frontend', 'Frontend'),
     ('grafik dizayn', 'Grafik dizayn'),
     ('3D dizayn', '3D dizayn'),

]


XONALAR = [
     ('A0', 'A0-xona'),
     ('A1', 'A1-xona'),
     ('A2', 'A2-xona'),
     ('A3', 'A3-xona'),
     ('A4', 'A4-xona'),
     ('A5', 'A5-xona'),
     ('B6', 'B6-xona'),
     ('B7', 'B7-xona'),
     ('B8', 'B8-xona'),
     ('B9', 'B9-xona'),
     ('B10', 'B10-xona'),

]









class Group(models.Model):
     nomi = models.CharField(max_length=250)
     mentor = models.ForeignKey(Teacher, on_delete=models.CASCADE)
     studentlar = models.ManyToManyField(Student, related_name='gruhlar')
     dars_vaqti = models.CharField(max_length=250)
     dars_kuni = models.CharField(max_length=250)
     kursi = models.CharField(max_length=250 , choices=KURSLAR)
     dars_xonasi = models.CharField(max_length=250, choices=XONALAR)


def __str__(self):
     return self.nomi
