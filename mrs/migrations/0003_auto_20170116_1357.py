# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-16 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mrs', '0002_auto_20170116_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='id',
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, related_name='movie_actors', through='mrs.Role', to='mrs.Person'),
        ),
        migrations.AlterField(
            model_name='role',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Movie_movie', to='mrs.Movie'),
        ),
        migrations.AlterField(
            model_name='role',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Movie_person', to='mrs.Person'),
        ),
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(max_length=64, primary_key=True, serialize=False),
        ),
    ]