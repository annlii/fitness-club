# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0033_auto_20160616_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('instructor_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('training_name', models.CharField(max_length=50)),
                ('start_time', models.TimeField(blank=True)),
                ('end_time', models.TimeField(default='00:00:00')),
                ('availability', models.IntegerField(default=15)),
                ('state', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='A', max_length=1)),
                ('date', models.DateField(default=datetime.date.today)),
                ('instructor', models.ForeignKey(to='club.Instructor')),
            ],
        ),
        migrations.CreateModel(
            name='TrnDesc',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('tr_name', models.CharField(max_length=50)),
                ('tr_desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='training',
            name='training_desc',
            field=models.ForeignKey(to='club.TrnDesc'),
        ),
    ]
