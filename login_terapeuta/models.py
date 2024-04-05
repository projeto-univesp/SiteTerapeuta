from django.db import models

class Terapeuta(models.Model):
    idTerapeuta = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    senha = models.CharField(max_length=100)