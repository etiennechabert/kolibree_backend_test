# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertoken',
            name='id',
        ),
        migrations.AlterField(
            model_name='usertoken',
            name='token',
            field=models.UUIDField(serialize=False, primary_key=True),
        ),
    ]
