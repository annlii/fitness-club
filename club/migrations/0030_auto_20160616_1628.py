# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0029_auto_20160616_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='training_desc',
            field=models.ForeignKey(to='club.TrnDesc'),
        ),
    ]
