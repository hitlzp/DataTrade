# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20170815_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='alldata',
            name='isaval',
            field=models.IntegerField(default=0),
        ),
    ]
