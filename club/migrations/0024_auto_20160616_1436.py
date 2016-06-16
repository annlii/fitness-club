# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0023_delete_trdesc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='instructor',
        ),
        migrations.DeleteModel(
            name='Instructor',
        ),
        migrations.DeleteModel(
            name='Training',
        ),
    ]
