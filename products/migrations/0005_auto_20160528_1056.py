# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20160528_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_type',
            field=models.PositiveSmallIntegerField(default=1, max_length=50, choices=[(1, 'news category'), (2, 'product category')], verbose_name='category type'),
        ),
    ]
