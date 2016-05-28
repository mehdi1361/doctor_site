# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category_is_enable'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_enable',
            field=models.BooleanField(verbose_name='enable', default=False),
        ),
        migrations.AddField(
            model_name='productimages',
            name='is_enable',
            field=models.BooleanField(verbose_name='enable', default=False),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='photo',
            field=models.ImageField(verbose_name='uploaded photo', upload_to='products/photos/%Y/%m/%d/%H/%M/'),
        ),
    ]
