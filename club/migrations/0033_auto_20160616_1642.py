# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0032_auto_20160616_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='training',
            name='training_desc',
        ),
        migrations.DeleteModel(
            name='Instructor',
        ),
        migrations.DeleteModel(
            name='Training',
        ),
        migrations.DeleteModel(
            name='TrnDesc',
        ),
    ]
