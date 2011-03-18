from datetime import datetime
from django.db import models

# Se um campo tem blank=True, a validacao na administracao do Django ira permitir a entrada de um valor vazio. 
# Se um campo tem blank=False, o campo sera obrigatorio.
# Null = True Se True, o Django ira gravar valores vazios como NULL no banco de dados. O padrao e False.

class Noticia(models.Model):
	data_entrada = models.DateTimeField('Publicacao da Noticia',default=datetime.now)
	data_saida = models.DateTimeField('Saida',null=True,blank=True)
	titulo = models.CharField(max_length=70)
	sub_titulo = models.CharField(max_length=250, blank=True)
	chapeu = models.CharField(max_length=50, blank=True)
	resumo = models.CharField(max_length=200, blank=True)
	texto = models.TextField()
	imagem_p = models.CharField(max_length=200)
	imagem_p_credito = models.CharField(max_length=50 ,blank=True)
	imagem_p_descricao = models.CharField(max_length=200 , blank=True)
	imagem_g = models.CharField(max_length=200 , blank=True)
	imagem_g_credito = models.CharField(max_length=50 , blank=True)
	imagem_g_descricao = models.CharField(max_length=200 , blank=True)
	view = models.IntegerField(max_length=5,default=0)
	ip = models.IPAddressField(null=True)
