from django.db import models

# Create your models here.
#python manage.py makemigrations
#python manage.py migrate
# Pilar (en singular)

class Pilar(models.Model):
    nombre = models.CharField(max_length=60)
    respiracion = models.CharField(max_length=30)
    edad = models.IntegerField(default=14)

    def __str__ (self):
        #acá puedo concatenar para que me muestre los datos que quiero en el admin.
        return "Pilar: " + self.nombre + "  " + str(self.edad),