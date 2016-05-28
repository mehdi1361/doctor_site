# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20160528_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(verbose_name='category description', blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(verbose_name='category title', max_length=50),
        ),
    ]
