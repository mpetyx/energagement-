# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20150731_0044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='ape_kwh',
        ),
        migrations.RemoveField(
            model_name='building',
            name='co2_lt_m2',
        ),
        migrations.RemoveField(
            model_name='building',
            name='co2_tn_m2',
        ),
        migrations.RemoveField(
            model_name='building',
            name='cosf',
        ),
        migrations.RemoveField(
            model_name='building',
            name='euro_forecast',
        ),
        migrations.RemoveField(
            model_name='building',
            name='euro_m2_electricity',
        ),
        migrations.RemoveField(
            model_name='building',
            name='euro_m2_liquidfuel',
        ),
        migrations.RemoveField(
            model_name='building',
            name='euro_m2_monthly',
        ),
        migrations.RemoveField(
            model_name='building',
            name='kwh_m2',
        ),
        migrations.RemoveField(
            model_name='building',
            name='kwh_m2_cooling',
        ),
        migrations.RemoveField(
            model_name='building',
            name='kwh_m2_heating',
        ),
        migrations.RemoveField(
            model_name='building',
            name='kwh_m2_lighting',
        ),
        migrations.RemoveField(
            model_name='building',
            name='kwh_m2_usagehours',
        ),
        migrations.RemoveField(
            model_name='building',
            name='kwh_m2_user',
        ),
        migrations.RemoveField(
            model_name='building',
            name='lt_m2',
        ),
        migrations.RemoveField(
            model_name='electricvehicle',
            name='co2_tn_user',
        ),
        migrations.RemoveField(
            model_name='electricvehicle',
            name='euro_forecast',
        ),
        migrations.RemoveField(
            model_name='electricvehicle',
            name='euro_m2_monthly',
        ),
        migrations.RemoveField(
            model_name='electricvehicle',
            name='euro_user',
        ),
        migrations.RemoveField(
            model_name='electricvehicle',
            name='kwh_user',
        ),
        migrations.RemoveField(
            model_name='streetlighting',
            name='ape_kwh',
        ),
        migrations.RemoveField(
            model_name='streetlighting',
            name='co2_lt_m2',
        ),
        migrations.RemoveField(
            model_name='streetlighting',
            name='co2_tn_km',
        ),
        migrations.RemoveField(
            model_name='streetlighting',
            name='cosf',
        ),
        migrations.RemoveField(
            model_name='streetlighting',
            name='euro_forecast',
        ),
        migrations.RemoveField(
            model_name='streetlighting',
            name='euro_line',
        ),
        migrations.RemoveField(
            model_name='streetlighting',
            name='euro_monthly',
        ),
        migrations.RemoveField(
            model_name='streetlighting',
            name='kwh_km',
        ),
        migrations.RemoveField(
            model_name='streetlighting',
            name='kwh_light',
        ),
        migrations.RemoveField(
            model_name='streetlighting',
            name='kwh_line',
        ),
        migrations.RemoveField(
            model_name='streetlighting',
            name='operatinglights_percentage',
        ),
        migrations.AddField(
            model_name='building',
            name='co2_lt',
            field=models.ManyToManyField(related_name='co2_lt_b', blank=True, null=True, to='myapp.Value'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='lt',
            field=models.ManyToManyField(related_name='lt', blank=True, null=True, to='myapp.Value'),
            preserve_default=True,
        ),
    ]
