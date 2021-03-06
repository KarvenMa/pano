# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-09 17:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, null=True, verbose_name='hover名称')),
                ('vector', models.CharField(max_length=100, null=True, verbose_name='向量/位置')),
                ('transition', models.CharField(max_length=300, null=True, verbose_name='转场动作')),
            ],
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.CharField(default=uuid.uuid1, max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SceneSpace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('space_name', models.CharField(max_length=20, null=True, verbose_name='空间名称')),
                ('ordinal', models.PositiveSmallIntegerField(default=1, verbose_name='序号')),
                ('scene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scene_id', to='panorama.Scene', verbose_name='场景')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('logo', models.ImageField(upload_to='seller-logo/')),
                ('phone', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('desc', models.CharField(max_length=300, null=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=100)),
                ('cache_url', models.CharField(max_length=100, null=True)),
                ('thumb_url', models.CharField(max_length=100, null=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator_id', to='panorama.Seller', verbose_name='创建者')),
            ],
        ),
        migrations.AddField(
            model_name='scenespace',
            name='space',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='space_id', to='panorama.Space', verbose_name='空间'),
        ),
        migrations.AddField(
            model_name='scene',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entry_id', to='panorama.Space', verbose_name='入口空间'),
        ),
        migrations.AddField(
            model_name='scene',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_id', to='panorama.Seller', verbose_name='商户'),
        ),
        migrations.AddField(
            model_name='hot',
            name='scene_space',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scene_space_id', to='panorama.SceneSpace', verbose_name='场景'),
        ),
    ]
