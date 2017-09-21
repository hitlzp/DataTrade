# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0020_datastate_auction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datastate_auction',
            name='dataid',
            field=models.ForeignKey(to='data.alldata_auction'),
        ),
    ]
