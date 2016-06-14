# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0005_training_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('instructor_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='training',
            old_name='time',
            new_name='start_time',
        ),
        migrations.AddField(
            model_name='training',
            name='day_of_week',
            field=models.CharField(default='Mon', max_length=3, choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wnd', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')]),
        ),
        migrations.AddField(
            model_name='training',
            name='end_time',
            field=models.TimeField(default='00:00:00'),
        ),
    ]
