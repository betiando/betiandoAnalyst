# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analyst', '0002_auto_20150405_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='datetime',
            new_name='created',
        ),
    ]
