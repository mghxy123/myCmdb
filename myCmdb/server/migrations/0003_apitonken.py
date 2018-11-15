# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='APITonken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.CharField(verbose_name='token值', max_length=32)),
                ('time', models.DateTimeField(verbose_name='生成时间', max_length=32)),
                ('user_id', models.CharField(verbose_name='token用户', max_length=32)),
            ],
        ),
    ]
