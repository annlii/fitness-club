# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0008_auto_20160715_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
