from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.
class Categoria(models.Model):
    nombre= models.CharField(max_length=50)
    def __str__(self) :
        return self.nombre

class Proyectos(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    imagen = models.ImageField(upload_to='imagenes_proyectos', null = True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=PROTECT)
    def __str__(self):
        return self.titulo+""+self.descripcion+""+str(self.fecha_creacion)

