# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analyst', '0003_auto_20150405_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='content',
            field=models.TextField(default=123),
            preserve_default=False,
        ),
    ]
