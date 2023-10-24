from django.db import models

class Alumno(models.Model):
    nombre = models.IntegerField(primary_key=True, verbose_name='Correo')
    password = models.CharField(max_length=50, verbose_name='Contra')

    def __str__(self):
        return self.password