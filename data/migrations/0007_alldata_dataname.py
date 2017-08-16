# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_datastate'),
    ]

    operations = [
        migrations.AddField(
            model_name='alldata',
            name='dataname',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
