# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0010_auto_20170823_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='alldata_auction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_time', models.DateTimeField(default=b'2012-05-15 21:05')),
                ('dataname', models.CharField(max_length=40, null=True)),
                ('file', models.FileField(upload_to=b'file')),
                ('file_name', models.CharField(max_length=50, null=True)),
                ('file_scale', models.CharField(max_length=20, null=True)),
                ('exchange', models.IntegerField(default=0)),
                ('introduce', models.TextField(null=True)),
                ('Show_demo', models.FileField(upload_to=b'file')),
                ('price', models.IntegerField(default=0)),
                ('limit', models.IntegerField(default=0)),
                ('limit_count', models.CharField(max_length=10, null=True)),
                ('type', models.CharField(max_length=10, null=True)),
                ('picture', models.FileField(upload_to=b'img')),
                ('isaval', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
