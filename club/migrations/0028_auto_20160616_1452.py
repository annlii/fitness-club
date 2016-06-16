# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0027_instructor_training'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrnDesc',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('tr_name', models.CharField(max_length=50)),
                ('tr_desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='training',
            name='training_name',
            field=models.ForeignKey(to='club.TrnDesc'),
        ),
    ]
