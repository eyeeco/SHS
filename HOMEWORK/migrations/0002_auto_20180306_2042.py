# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-06 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOMEWORK', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='data_class',
            field=models.IntegerField(choices=[(1, '人工智能实践班'), (2, '虚拟现实实践班'), (3, '智能硬件实践班')], default=2, verbose_name='所属实践班'),
        ),
    ]
