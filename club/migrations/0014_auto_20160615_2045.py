# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0013_auto_20160615_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekday',
            name='day_number',
            field=models.IntegerField(default='Monday', primary_key=True, serialize=False, choices=[('A', 'Monday'), ('B', 'Tuesday'), ('C', 'Wednesday'), ('D', 'Thursday'), ('5m', 'Friday'), ('6m', 'Saturday'), ('7m', 'Sunday')]),
        ),
    ]
