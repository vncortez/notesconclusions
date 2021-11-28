import re
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.



class Title(models.Model):
    class TypeOf(models.TextChoices):
        a = '#'
        b = '##'
        c = '###'
    text = models.CharField(max_length=30)
    order = models.IntegerField()
    type_of = models.CharField(max_length=3, choices=TypeOf.choices)

class TypeOfText(models.Model):
    text = models.CharField(max_length=30)

class NodeText(models.Model):
    text = models.TextField(max_length=1500)
    titulos = models.ManyToManyField(to=Title)
    tipo_texto = models.ForeignKey(to=TypeOfText, on_delete=models.CASCADE, related_name='textos')
    usuario = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    
    
    @property
    def author(self):
        return self.usuario.username
    
    @property
    def type_of_text(self):
        return self.tipo_texto.text
    
