# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0012_auto_20160615_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekday',
            name='day_number',
            field=models.IntegerField(primary_key=True, serialize=False, choices=[('1m', 'Monday'), ('2m', 'Tuesday'), ('3m', 'Wednesday'), ('4m', 'Thursday'), ('5m', 'Friday'), ('6m', 'Saturday'), ('7m', 'Sunday')], default='1m'),
        ),
    ]
