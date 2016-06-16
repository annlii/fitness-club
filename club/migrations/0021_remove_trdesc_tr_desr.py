# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0020_auto_20160616_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trdesc',
            name='tr_desr',
        ),
    ]
