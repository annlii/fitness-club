# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0007_auto_20160713_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
