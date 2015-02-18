# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pollen_type', models.CharField(max_length=50)),
                ('plant_tree', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AllergenInGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allergen', models.ForeignKey(to='polen.Allergen')),
            ],
            options={
                'verbose_name_plural': 'Allergens in group',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('low_level_bottom_limit', models.PositiveSmallIntegerField(default=0)),
                ('medium_level_bottom_limit', models.PositiveSmallIntegerField(default=0)),
                ('high_level_bottom_limit', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('value', models.PositiveSmallIntegerField(default=0, blank=True)),
                ('allergen', models.ForeignKey(to='polen.Allergen')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('latitude', models.FloatField(default=0, null=True, blank=True)),
                ('longitude', models.FloatField(default=0, null=True, blank=True)),
                ('height', models.PositiveSmallIntegerField(default=0, blank=True)),
                ('height_from_street_level', models.PositiveSmallIntegerField(default=0, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='allergeningroup',
            name='group',
            field=models.ForeignKey(to='polen.Group'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='allergeningroup',
            unique_together=set([('allergen', 'group')]),
        ),
        migrations.AddField(
            model_name='allergen',
            name='group',
            field=models.ForeignKey(to='polen.Group'),
            preserve_default=True,
        ),
    ]
