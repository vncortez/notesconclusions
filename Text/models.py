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
    
    def __str__(self):
        return f'{self.type_of} {self.text}'
    

class TypeOfText(models.Model):
    text = models.CharField(max_length=30)
    
    def __str__(self):
        return self.text

class NodeText(models.Model):
    text = models.TextField(max_length=1500)
    titulos = models.ManyToManyField(to=Title)
    tipo_texto = models.ForeignKey(to=TypeOfText, on_delete=models.CASCADE, related_name='textos')
    usuario = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    sub_titulo = models.CharField(max_length=100)
    publicavel = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now=True)
    
    @property
    def author(self):
        return self.usuario.username
    
    @property
    def type_of_text(self):
        return self.tipo_texto.text
    
    def __str__(self):
        return f'{self.sub_titulo}'
    
