# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0021_remove_trdesc_tr_desr'),
    ]

    operations = [
        migrations.AddField(
            model_name='trdesc',
            name='tr_desc',
            field=models.CharField(max_length=200, default='Desc'),
        ),
        migrations.AlterField(
            model_name='training',
            name='training_name',
            field=models.CharField(max_length=50),
        ),
    ]
