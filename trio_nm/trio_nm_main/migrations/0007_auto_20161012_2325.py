# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-12 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trio_nm_main', '0006_calendarevent_end_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achieverprofile',
            name='posting_date',
        ),
        migrations.RemoveField(
            model_name='calendarevent',
            name='end_date',
        ),
        migrations.AddField(
            model_name='achieverprofile',
            name='optional_posting_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='calendarevent',
            name='optional_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]