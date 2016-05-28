# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20160528_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='avatar',
            field=models.ImageField(verbose_name='avatar', upload_to='category/photos/%Y/%m/%d/%H/%M/', blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_type',
            field=models.PositiveSmallIntegerField(verbose_name='category type', choices=[(1, 'public category'), (2, 'news category'), (3, 'product category')], default=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='avatar',
            field=models.ImageField(verbose_name='avatar', upload_to='products/photos/%Y/%m/%d/%H/%M/', blank=True),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='photo',
            field=models.ImageField(verbose_name='uploaded photo', upload_to='productsimages/photos/%Y/%m/%d/%H/%M/'),
        ),
    ]
