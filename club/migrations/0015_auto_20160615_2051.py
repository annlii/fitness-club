# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0014_auto_20160615_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='day_of_week',
            field=models.CharField(default='1', max_length=1, choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday'), ('7', 'Sunday')]),
        ),
        migrations.DeleteModel(
            name='WeekDay',
        ),
    ]
