from django.db import models
class Personas(models. Model):
  cedula = models.CharField(max_length= 10, unique= True)
  nombre = models.CharField(max_length=255)
  apellido = models.CharField(max_length=255)
  telefono = models.CharField(max_length=12)
  direccion= models.CharField(max_length=255)
  correo= models.CharField(max_length=32, unique=True)
  fecha_nacimiento= models.DateField()

  def __str__(self):
    return '%s %s %s %s %s %s %s'%(self.cedula, self.nombre,self.apellido,self.telefono,self.direccion, self.correo,self.fecha_nacimiento)
  

  class Empresas (models.Model):
    nombres= models.CharField (max_length=255)
    correo= models.CharField(max_length=32, unique=True)
    def __str__(self):
        return '%s %s'%(self.nombre,self.correo)
        



# Create your models here.
