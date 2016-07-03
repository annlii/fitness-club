# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0003_remove_participant_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='phone',
            field=models.CharField(max_length=10, default='0000000000'),
        ),
        migrations.AddField(
            model_name='participant',
            name='training',
            field=models.ForeignKey(to='club.Training', default=1),
            preserve_default=False,
        ),
    ]
