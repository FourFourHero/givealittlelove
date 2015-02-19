# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gall', '0005_auto_20150219_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='activation',
            name='coupon_id',
            field=models.IntegerField(default=-1),
            preserve_default=True,
        ),
    ]
