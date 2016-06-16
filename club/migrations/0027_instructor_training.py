# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0026_auto_20160616_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('instructor_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('training_name', models.CharField(max_length=50)),
                ('start_time', models.TimeField(blank=True)),
                ('end_time', models.TimeField(default='00:00:00')),
                ('availability', models.IntegerField(default=15)),
                ('state', models.CharField(max_length=1, default='A', choices=[('A', 'Active'), ('I', 'Inactive')])),
                ('date', models.DateField(default=datetime.date.today)),
                ('instructor', models.ForeignKey(to='club.Instructor')),
            ],
        ),
    ]
