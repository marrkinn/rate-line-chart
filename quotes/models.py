# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Quotes(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=5)

class Post(models.Model):
    dia_inicio = models.DateField()
    dia_fim = models.DateField()
    moeda = models.CharField(max_length=50, choices=[
        ('BRL', 'Real - R$'),
        ('EUR', 'Euro - €'),
        ('JPY', 'Iene - ¥'),
    ])
