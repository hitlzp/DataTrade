# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_mydata_owner'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='mydata',
            new_name='alldata',
        ),
    ]
