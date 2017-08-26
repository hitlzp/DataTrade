# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_alldata_isaval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alldata',
            name='limit_count',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
