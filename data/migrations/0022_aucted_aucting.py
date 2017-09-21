# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0021_auto_20170921_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='aucted',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_time', models.DateTimeField(default=b'2012-05-15 21:05')),
                ('price', models.IntegerField(default=0)),
                ('result', models.IntegerField(default=0)),
                ('buyer', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('dataid', models.ForeignKey(to='data.alldata_auction')),
            ],
        ),
        migrations.CreateModel(
            name='aucting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_time', models.DateTimeField(default=b'2012-05-15 21:05')),
                ('price', models.IntegerField(default=0)),
                ('buyer', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('dataid', models.ForeignKey(to='data.alldata_auction')),
            ],
        ),
    ]
