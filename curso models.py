from django.db import models

# Create your models here.
class curso(models.Model):

    nome = models.CharField(max_lenght=100)
    codigo = models.CharField(max_lenght=100)
