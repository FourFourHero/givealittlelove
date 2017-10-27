# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gall', '0003_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambassador',
            name='code',
            field=models.CharField(unique=True, max_length=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ambassador',
            name='email',
            field=models.EmailField(unique=True, max_length=254),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(unique=True, max_length=17),
            preserve_default=True,
        ),
    ]
