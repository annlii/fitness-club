# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_auto_20160703_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
