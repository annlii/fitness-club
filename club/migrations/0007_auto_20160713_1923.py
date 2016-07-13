# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0006_auto_20160708_2224'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Participant',
            new_name='Booking',
        ),
    ]
