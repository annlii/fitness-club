# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0016_auto_20160615_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrDesc',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('tr_name', models.CharField(default='Zumba', max_length=50)),
                ('tr_desr', models.CharField(default='Description', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='training',
            name='training_name',
            field=models.ForeignKey(to='club.TrDesc'),
        ),
    ]
