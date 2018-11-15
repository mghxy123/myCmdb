# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ip', models.CharField(verbose_name='服务器IP', max_length=32)),
                ('mac', models.CharField(verbose_name='服务器MAC', max_length=32)),
                ('cpu', models.CharField(verbose_name='服务器CPU', max_length=32)),
                ('memory', models.CharField(verbose_name='服务器内存P', max_length=32)),
                ('hostname', models.CharField(verbose_name='服务器主机', max_length=32)),
                ('isalive', models.CharField(verbose_name='服务器状态', max_length=32)),
            ],
        ),
    ]
