# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0010_auto_20160715_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='counter',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='training',
            name='availability',
            field=models.PositiveIntegerField(default=15),
        ),
    ]
