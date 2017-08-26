# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_buydata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buydata',
            old_name='buyer_id',
            new_name='buyer',
        ),
        migrations.RenameField(
            model_name='buydata',
            old_name='dataid',
            new_name='data',
        ),
    ]
