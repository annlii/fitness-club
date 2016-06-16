# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0025_instructor_training'),
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
