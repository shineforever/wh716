# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-02 09:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baoming', '0013_auto_20170430_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='baoming.Club', verbose_name='\u4ff1\u4e50\u90e8\u540d\u79f0'),
        ),
    ]