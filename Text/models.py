from django.db import models
from django.db.models.fields import TextField

# Create your models here.



class Title (models.Model):
    class TypeOf(models.Choices):
        a = '#'
        b = '##'
        c = '###'
    text = models.CharField(max_length=30)
    order = models.IntegerField()
    type_of = models.CharField(choices=TypeOf.choices())

class TypeOfText(models.Model):
    text = models.CharField(max_length=30)


class NodeText(models.Model):
    text = models.TextField(max_length=500)
    models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
