# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-05 13:55
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170405_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='lnglat',
            field=models.CharField(blank=True, help_text='Optional 위도/경도 포맷으로 입력', max_length=50, validators=[blog.models.lnglat_validator]),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('d', 'draft'), ('p', 'published'), ('w', 'withdrawn')], max_length=1),
        ),
    ]
