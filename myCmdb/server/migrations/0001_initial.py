# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='api_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='接口名称', max_length=32)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='接口描述')),
                ('doc', models.CharField(verbose_name='接口说明', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='CMDBUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(verbose_name='用户账号', max_length=32)),
                ('password', models.CharField(verbose_name='用户密码', max_length=32)),
                ('nickname', models.CharField(verbose_name='用户姓名', max_length=32)),
                ('phone', models.CharField(verbose_name='用户手机号', max_length=32)),
                ('email', models.EmailField(verbose_name='用户邮箱', max_length=32)),
                ('photo', models.ImageField(verbose_name='用户头像', max_length=32, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Cpu_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('processor', models.CharField(max_length=32, blank=True, null=True)),
                ('vendor_id', models.CharField(max_length=32, blank=True, null=True)),
                ('cpu_family', models.CharField(max_length=32, blank=True, null=True)),
                ('model', models.CharField(max_length=32, blank=True, null=True)),
                ('model_name', models.CharField(max_length=32, blank=True, null=True)),
                ('stepping', models.CharField(max_length=32, blank=True, null=True)),
                ('microcode', models.CharField(max_length=32, blank=True, null=True)),
                ('cpu_MHz', models.CharField(max_length=32, blank=True, null=True)),
                ('cache_size', models.CharField(max_length=32, blank=True, null=True)),
                ('physical_id', models.CharField(max_length=32, blank=True, null=True)),
                ('siblings', models.CharField(max_length=32, blank=True, null=True)),
                ('core_id', models.CharField(max_length=32, blank=True, null=True)),
                ('cpu_cores', models.CharField(max_length=32, blank=True, null=True)),
                ('apicid', models.CharField(max_length=32, blank=True, null=True)),
                ('initial_apicid', models.CharField(max_length=32, blank=True, null=True)),
                ('fpu', models.CharField(max_length=32, blank=True, null=True)),
                ('fpu_exception', models.CharField(max_length=32, blank=True, null=True)),
                ('cpuid_level', models.CharField(max_length=32, blank=True, null=True)),
                ('wp', models.CharField(max_length=32, blank=True, null=True)),
                ('flags', models.CharField(max_length=32, blank=True, null=True)),
                ('bogomips', models.CharField(max_length=32, blank=True, null=True)),
                ('clflush_size', models.CharField(max_length=32, blank=True, null=True)),
                ('cache_alignment', models.CharField(max_length=32, blank=True, null=True)),
                ('address_sizes', models.CharField(max_length=32, blank=True, null=True)),
                ('power_management', models.CharField(max_length=32, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Memory_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('MemTotal', models.CharField(max_length=32, blank=True, null=True)),
                ('MemFree', models.CharField(max_length=32, blank=True, null=True)),
                ('MemAvailable', models.CharField(max_length=32, blank=True, null=True)),
                ('Buffers', models.CharField(max_length=32, blank=True, null=True)),
                ('Cached', models.CharField(max_length=32, blank=True, null=True)),
                ('SwapCached', models.CharField(max_length=32, blank=True, null=True)),
                ('Active', models.CharField(max_length=32, blank=True, null=True)),
                ('Inactive', models.CharField(max_length=32, blank=True, null=True)),
                ('Active_anon', models.CharField(max_length=32, blank=True, null=True)),
                ('Inactive_anon', models.CharField(max_length=32, blank=True, null=True)),
                ('Active_file', models.CharField(max_length=32, blank=True, null=True)),
                ('Inactive_file', models.CharField(max_length=32, blank=True, null=True)),
                ('Unevictable', models.CharField(max_length=32, blank=True, null=True)),
                ('Mlocked', models.CharField(max_length=32, blank=True, null=True)),
                ('SwapTotal', models.CharField(max_length=32, blank=True, null=True)),
                ('SwapFree', models.CharField(max_length=32, blank=True, null=True)),
                ('Dirty', models.CharField(max_length=32, blank=True, null=True)),
                ('Writeback', models.CharField(max_length=32, blank=True, null=True)),
                ('AnonPages', models.CharField(max_length=32, blank=True, null=True)),
                ('Mapped', models.CharField(max_length=32, blank=True, null=True)),
                ('Shmem', models.CharField(max_length=32, blank=True, null=True)),
                ('Slab', models.CharField(max_length=32, blank=True, null=True)),
                ('SReclaimable', models.CharField(max_length=32, blank=True, null=True)),
                ('SUnreclaim', models.CharField(max_length=32, blank=True, null=True)),
                ('KernelStack', models.CharField(max_length=32, blank=True, null=True)),
                ('PageTables', models.CharField(max_length=32, blank=True, null=True)),
                ('NFS_Unstable', models.CharField(max_length=32, blank=True, null=True)),
                ('Bounce', models.CharField(max_length=32, blank=True, null=True)),
                ('WritebackTmp', models.CharField(max_length=32, blank=True, null=True)),
                ('CommitLimit', models.CharField(max_length=32, blank=True, null=True)),
                ('Committed_AS', models.CharField(max_length=32, blank=True, null=True)),
                ('VmallocTotal', models.CharField(max_length=32, blank=True, null=True)),
                ('VmallocUsed', models.CharField(max_length=32, blank=True, null=True)),
                ('VmallocChunk', models.CharField(max_length=32, blank=True, null=True)),
                ('HardwareCorrupted', models.CharField(max_length=32, blank=True, null=True)),
                ('AnonHugePages', models.CharField(max_length=32, blank=True, null=True)),
                ('HugePages_Total', models.CharField(max_length=32, blank=True, null=True)),
                ('HugePages_Free', models.CharField(max_length=32, blank=True, null=True)),
                ('HugePages_Rsvd', models.CharField(max_length=32, blank=True, null=True)),
                ('HugePages_Surp', models.CharField(max_length=32, blank=True, null=True)),
                ('Hugepagesize', models.CharField(max_length=32, blank=True, null=True)),
                ('DirectMap4k', models.CharField(max_length=32, blank=True, null=True)),
                ('DirectMap2M', models.CharField(max_length=32, blank=True, null=True)),
                ('DirectMap1G', models.CharField(max_length=32, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Server_cpu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('server_id', models.IntegerField()),
                ('cpu_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Server_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ip', models.CharField(verbose_name='服务器IP', max_length=32)),
                ('mac', models.CharField(verbose_name='服务器物理地址', max_length=32)),
                ('cpu', models.CharField(verbose_name='服务器cpu', max_length=32)),
                ('memory', models.CharField(verbose_name='服务器内存', max_length=32)),
                ('disk', models.CharField(verbose_name='服务器硬盘', max_length=32)),
                ('isalive', models.CharField(verbose_name='服务器状态', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='server_memory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('server_id', models.IntegerField()),
                ('memory_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='cmdbuser',
            name='service',
            field=models.ManyToManyField(to='server.Server_info'),
        ),
    ]
