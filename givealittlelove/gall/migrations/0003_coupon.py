# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gall', '0002_activation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=17)),
                ('sent', models.BooleanField(default=False)),
                ('activation_id', models.IntegerField(default=-1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
                'db_table': 'gall_coupon',
            },
            bases=(models.Model,),
        ),
    ]
