# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0017_auto_20160616_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='training_description',
        ),
    ]
