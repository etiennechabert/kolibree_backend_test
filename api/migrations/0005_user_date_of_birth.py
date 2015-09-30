# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_user_usertoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2015, 9, 29, 19, 33, 6, 150950, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
