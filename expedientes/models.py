from django.db import models

class Expediente(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Documento(models.Model):
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE, related_name="documentos")
    archivo = models.FileField(upload_to="documentos/")

    def __str__(self):
        return f"Documento de {self.expediente.nombre}"

