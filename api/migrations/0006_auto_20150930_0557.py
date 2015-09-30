# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_user_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertoken',
            name='creation_dateTime',
            field=models.DateTimeField(),
        ),
    ]
