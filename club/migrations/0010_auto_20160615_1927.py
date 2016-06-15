# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0009_auto_20160615_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekday',
            name='day_number',
            field=models.IntegerField(primary_key=True, serialize=False, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')]),
        ),
    ]
