# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_auto_20160613_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='state',
            field=models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=1, default='A'),
        ),
    ]
