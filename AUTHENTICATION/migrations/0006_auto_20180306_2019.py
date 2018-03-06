# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-06 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AUTHENTICATION', '0005_studentinfo_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacherinfo',
            options={'verbose_name': '教师信息'},
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='status',
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='stu_class',
            field=models.IntegerField(choices=[(1, '人工智能实践班'), (2, '虚拟现实实践班'), (3, '智能硬件实践班')], default=1, verbose_name='实践班'),
        ),
        migrations.AddField(
            model_name='teacherinfo',
            name='tea_class',
            field=models.IntegerField(choices=[(1, '人工智能实践班'), (2, '虚拟现实实践班'), (3, '智能硬件实践班')], default=1, verbose_name='实践班'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='Title',
            field=models.IntegerField(choices=[(0, '工程师'), (1, '高级工程师'), (2, '讲师'), (3, '副教授'), (4, '教授')], verbose_name='职称'),
        ),
    ]
