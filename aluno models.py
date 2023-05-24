from django.db import models

# Create your models here.





class alunos (models.Model):

    nome = models.CharField(max_length=50)
    sexo = models.CharField(max_lenght=10)
    matricula = models.CharField(max_length=50)
    datanascimento = models.Datefield(max_lenght=20)
