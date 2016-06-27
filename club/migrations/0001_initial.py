# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('start_time', models.TimeField(blank=True)),
                ('end_time', models.TimeField(default='00:00:00')),
                ('availability', models.IntegerField(default=15)),
                ('state', models.CharField(max_length=1, choices=[('A', 'Active'), ('I', 'Inactive')], default='A')),
                ('training_date', models.DateField(default=datetime.date.today)),
                ('instructor', models.ForeignKey(to='club.Instructor')),
            ],
        ),
        migrations.CreateModel(
            name='TrnDesc',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='training',
            name='name',
            field=models.ForeignKey(to='club.TrnDesc'),
        ),
    ]
