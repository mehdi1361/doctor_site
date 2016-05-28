# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20160528_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_enable',
            field=models.BooleanField(verbose_name='enable', default=False),
        ),
    ]
