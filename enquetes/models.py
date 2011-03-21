from django.db import models
from datetime import datetime

# Create your models here.

class Enquete(models.Model):
	questao = models.CharField(max_length=200)
	data_publicacao = models.DateTimeField(default=datetime.now,blank=True)
	data_entrada = models.DateTimeField('Entrada',default=datetime.now)
	data_saida = models.DateTimeField('Saida',null=True,blank=True)

class Escolha(models.Model):
    enquete = models.ForeignKey(Enquete)
    escolha = models.CharField(max_length=200)
    votos = models.IntegerField()
