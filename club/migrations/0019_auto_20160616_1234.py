# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0018_remove_training_training_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trdesc',
            name='id',
        ),
        migrations.AlterField(
            model_name='trdesc',
            name='tr_name',
            field=models.CharField(primary_key=True, default='Zumba', max_length=50, serialize=False),
        ),
    ]
