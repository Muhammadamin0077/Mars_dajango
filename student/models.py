from django.db import models

# Create your models here.

class Student(models.Model):
      ism_familya = models.CharField(max_length=250)
      yosh = models.IntegerField()
      coinlar = models.IntegerField()
      xp_level = models.IntegerField()
      rasm = models.ImageField(upload_to='rasmlar/')

      def __str__(self):
         return self.ism_familya