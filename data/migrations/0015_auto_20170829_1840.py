# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0014_auto_20170829_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alldata',
            name='type',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='alldata_bargain',
            name='type',
            field=models.IntegerField(default=0),
        ),
    ]
