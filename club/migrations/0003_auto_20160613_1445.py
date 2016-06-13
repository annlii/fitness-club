# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_training_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='time',
            field=models.TimeField(),
        ),
    ]
