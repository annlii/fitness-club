# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0005_auto_20160703_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
