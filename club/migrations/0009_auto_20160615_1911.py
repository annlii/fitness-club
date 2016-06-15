# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0008_auto_20160615_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeekDay',
            fields=[
                ('day_number', models.IntegerField(primary_key=True, serialize=False, choices=[('1', 'Mon'), ('2', 'Tue'), ('3', 'Wed'), ('4', 'Thu'), ('5', 'Fri'), ('6', 'Sat'), ('7', 'Sun')])),
                ('day_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='WeekDays',
        ),
        migrations.AlterField(
            model_name='training',
            name='day_of_week',
            field=models.ForeignKey(to='club.WeekDay'),
        ),
    ]
