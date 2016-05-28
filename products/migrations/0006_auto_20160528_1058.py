# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20160528_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(null=True, to='products.Category', related_name='children', verbose_name='parent category', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='parent',
            field=models.ForeignKey(null=True, to='products.Product', related_name='children', verbose_name='parent product', blank=True),
        ),
    ]
