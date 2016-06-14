# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0006_auto_20160614_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='instructor',
            field=models.ForeignKey(to='club.Instructor'),
        ),
    ]
