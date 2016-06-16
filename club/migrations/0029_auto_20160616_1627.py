# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0028_auto_20160616_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='training_desc',
            field=models.ForeignKey(to='club.TrnDesc', default='desc'),
        ),
        migrations.AlterField(
            model_name='training',
            name='training_name',
            field=models.CharField(max_length=50),
        ),
    ]
