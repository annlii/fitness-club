# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('training_name', models.CharField(max_length=50)),
                ('training_description', models.CharField(max_length=200)),
                ('instructor', models.CharField(max_length=30)),
                ('availability', models.IntegerField(default=15)),
            ],
        ),
    ]
