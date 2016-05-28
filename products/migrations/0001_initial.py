# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('category_type', models.CharField(max_length=50, default=1, verbose_name='category type', choices=[(1, 'news category'), (2, 'product category')])),
                ('create_time', models.DateTimeField(verbose_name='category create time')),
                ('title', models.TextField(verbose_name='category description', blank=True)),
                ('slug', models.SlugField(help_text='Use ascii characters', verbose_name='slug title')),
                ('avatar', models.ImageField(upload_to='', verbose_name='avatar', blank=True)),
            ],
            options={
                'db_table': 'categories',
                'ordering': ['title', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=50, verbose_name='product title')),
                ('create_time', models.DateTimeField(verbose_name='product create time', auto_now_add=True)),
                ('slug', models.SlugField(help_text='Use ascii characters', verbose_name='slug title')),
                ('avatar', models.ImageField(upload_to='', verbose_name='avatar', blank=True)),
                ('category', models.ManyToManyField(verbose_name='categories', to='products.Category', blank=True)),
                ('parent', models.ForeignKey(related_name='children', to='products.Product', blank=True, null=True, verbose_name='parent category')),
            ],
            options={
                'db_table': 'products',
                'ordering': ['title', 'id'],
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created_time', models.DateTimeField(verbose_name='creation time', auto_now_add=True)),
                ('photo', models.ImageField(upload_to='flyers/photos/%Y/%m/%d/%H/%M/', verbose_name='uploaded photo')),
                ('product', models.ForeignKey(related_name='photos', to='products.Product', null=True, on_delete=django.db.models.deletion.SET_NULL, verbose_name='product')),
            ],
            options={
                'db_table': 'products_image',
                'ordering': ['created_time', 'product', 'id'],
            },
        ),
    ]
