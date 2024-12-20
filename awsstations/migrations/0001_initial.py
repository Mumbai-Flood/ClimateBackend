# Generated by Django 5.1.3 on 2024-11-18 08:56

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AWSStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('rainfall', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DaywisePrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('day1_rainfall', models.FloatField(default=0)),
                ('day2_rainfall', models.FloatField(default=0)),
                ('day3_rainfall', models.FloatField(default=0)),
                ('station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='awsstations.awsstation')),
            ],
        ),
        migrations.CreateModel(
            name='HourlyPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('hr_24_rainfall', models.JSONField(default=dict)),
                ('station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='awsstations.awsstation')),
            ],
        ),
        migrations.CreateModel(
            name='StationData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rainfall', models.FloatField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awsstations.awsstation')),
            ],
        ),
        migrations.CreateModel(
            name='TrainStation',
            fields=[
                ('station_code', models.IntegerField(primary_key=True, serialize=False)),
                ('station_name', models.CharField(max_length=100)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('WarningLevel', models.IntegerField(default=0)),
                ('neareststation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='awsstations.awsstation')),
            ],
        ),
    ]
