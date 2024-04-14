from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    fecha_expiracion = models.DateField()
    class Meta:
        db_table = 'mi_proyecto_tarea'
        
    def __str__(self):
        return self.titulo
        