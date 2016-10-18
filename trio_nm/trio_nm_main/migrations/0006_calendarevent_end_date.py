# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-12 21:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trio_nm_main', '0005_achieverprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarevent',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]