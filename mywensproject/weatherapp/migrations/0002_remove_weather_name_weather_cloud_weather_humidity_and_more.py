# Generated by Django 4.2.7 on 2023-12-03 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='name',
        ),
        migrations.AddField(
            model_name='weather',
            name='cloud',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='humidity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='pressure',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='rain',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='temp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='utc_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='visibility',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='wind_speed',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
