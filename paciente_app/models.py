from django.db import models

# Create your models here.
class Paciente(models.Model):
    id_paciente = models.PositiveSmallIntegerField(primary_key=True)  # Definir id_paciente
    id_producto = models.CharField(max_length=100)  # Campo id_producto
    id_cliente = models.CharField(max_length=100)  # Campo id_cliente
    calificacion = models.CharField(max_length=100)  # Campo calificación
    comentario = models.CharField(max_length=100)  # Campo comentario
    fecha_reseña = models.DateField()  # Cambié a DateField para solo manejar fecha
    estado = models.CharField(max_length=100)  # Campo estado

    def __str__(self):
        return self.comentario
