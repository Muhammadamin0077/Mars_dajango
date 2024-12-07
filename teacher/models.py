from django.db import models

# Create your models here.

class Teacher(models.Model):
      ism_familya = models.CharField(max_length=250)
      yosh = models.IntegerField()
      telefon = models.CharField(max_length=20)
      oyligi = models.IntegerField()
      rasm = models.ImageField(upload_to='rasmlar/')
      email = models.EmailField
      username = models.CharField(max_length=120)


      def __str__(self):
         return self.ism_familya
