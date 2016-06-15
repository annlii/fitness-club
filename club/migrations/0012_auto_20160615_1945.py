# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0011_auto_20160615_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weekday',
            name='day_name',
        ),
        migrations.AlterField(
            model_name='weekday',
            name='day_number',
            field=models.IntegerField(default='1', serialize=False, primary_key=True, choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday'), ('7', 'Sunday')]),
        ),
    ]
