# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gall', '0004_auto_20150219_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambassador',
            name='email',
            field=models.EmailField(max_length=254),
            preserve_default=True,
        ),
    ]
