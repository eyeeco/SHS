# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-28 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AUTHENTICATION', '0003_studentinfo_homework_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='个人简介'),
        ),
    ]