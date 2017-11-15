# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-05 11:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scallop', '0004_auto_20171102_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='applytype',
            name='name',
            field=models.CharField(max_length=32, null=True, verbose_name='申请表类型'),
        ),
        migrations.AlterField(
            model_name='activityapply',
            name='apply_type',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='scallop.ApplyType', verbose_name='申请表类型'),
        ),
    ]