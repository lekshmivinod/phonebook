# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-06 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wrongnumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Phonenumber', models.IntegerField()),
            ],
            options={
                'db_table': 'wrongnumber',
            },
        ),
    ]
