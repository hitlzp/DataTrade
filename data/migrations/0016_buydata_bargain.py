# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0015_auto_20170829_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='buydata_bargain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_time', models.DateTimeField(default=b'2012-05-15 21:05')),
                ('price', models.IntegerField(default=0)),
                ('state', models.IntegerField(default=0)),
                ('buyer_detail', models.TextField(null=True)),
                ('seller_detail', models.TextField(null=True)),
                ('buyer_id', models.ForeignKey(related_name='buyer', to=settings.AUTH_USER_MODEL, null=True)),
                ('dataid', models.ForeignKey(to='data.alldata_bargain', null=True)),
                ('trader_id', models.ForeignKey(related_name='trader', to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
