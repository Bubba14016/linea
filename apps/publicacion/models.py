from django.db import models

# Create your models here.

class publicacion(models.Model):
	titulo=models.CharField(max_length=50)
	contenido=models.TextField()
	fecha=models.DateField()
	image = models.ImageField(upload_to='imagenes/')
	archivo=models.FileField(upload_to='archivos/')
