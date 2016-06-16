# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0019_auto_20160616_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='trdesc',
            name='id',
            field=models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trdesc',
            name='tr_desr',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='trdesc',
            name='tr_name',
            field=models.CharField(max_length=50),
        ),
    ]
