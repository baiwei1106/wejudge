# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-18 06:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0004_auto_20160217_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
        migrations.AddField(
            model_name='arrangement',
            name='parent_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_course', to='education.Course'),
        ),
    ]
