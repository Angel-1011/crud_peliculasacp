from django.db import models
import os

# Create your models here.

class peliculas(models.Model):
    nombre= models.CharField(max_length=100)
    categoria= models.CharField(max_length=100)
    año= models.DateField()
    # Carga de archivos
    foto = models.ImageField(upload_to='peliculas_fotos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.categoria}"
    
    # Eliminar imagen cuando se elimina la pelicula
    def delete(self, *args, **kwargs):
        if self.foto:
            if os.path.isfile(self.foto.path):
                os.remove(self.foto.path)
            super().delete(*args, **kwargs)
        
