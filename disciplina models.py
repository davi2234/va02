from django.db import models

# Create your models here.
class disciplina(models.Model):

    nome = models.CharField(max_lenght=100)
    codigo = models.SmallIntegerField()
