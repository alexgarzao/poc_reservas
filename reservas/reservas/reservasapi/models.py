from __future__ import unicode_literals

from django.db import models

import datetime


class Merchant(models.Model):
    cnpj = models.CharField(max_length=14)
    name = models.TextField(default='', blank=True, max_length=50)

    def __str__(self):
        return self.name


class MerchantItem(models.Model):
    merchant = models.ForeignKey(Merchant)
    description = models.TextField(max_length=40)                                               # Descricao do item.
    start_date = models.DateField(default=datetime.date.today())                                # Periodo inicial para uso.
    end_date = models.DateField(default=datetime.date.today() + datetime.timedelta(days=365))   # Periodo final para uso.
    start_time = models.TimeField(default=datetime.time(8, 00))                                 # Horario inicial para uso.
    end_time = models.TimeField(default=datetime.time(23, 00))                                  # Horario final para uso.
    price = models.DecimalField(max_digits=6, decimal_places=2)                                 # Preco.
    minimum_purchase = models.IntegerField(default=1)                                           # Compra minima.
    maximum_per_day = models.IntegerField(default=9999)                                         # Maximo de vendas por dia.
    # TODO: quais dias da semana eh ofertado!

    def __str__(self):
        return self.description
