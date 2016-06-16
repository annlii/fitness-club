# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0022_auto_20160616_1320'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TrDesc',
        ),
    ]
