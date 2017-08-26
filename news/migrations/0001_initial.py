# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(default=b'')),
                ('date', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=10)),
                ('author', models.CharField(max_length=20)),
            ],
        ),
    ]
