# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your models here.
from django.db import models

class wrongnumber(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Phonenumber=models.CharField(max_length=50)

    class Meta:
      db_table="wrongnumber"
