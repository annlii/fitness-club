# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0015_auto_20160615_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='day_of_week',
        ),
        migrations.AddField(
            model_name='training',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
