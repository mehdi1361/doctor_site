# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20160528_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_type',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='category type', choices=[(1, 'news category'), (2, 'product category')]),
        ),
    ]
