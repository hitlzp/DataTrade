# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_auto_20170823_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buydata',
            name='data',
            field=models.ForeignKey(to='data.alldata', null=True),
        ),
    ]
