# Generated by Django 5.1.3 on 2024-11-18 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSFormData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('feet', models.IntegerField(blank=True, null=True)),
                ('inch', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_text', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('sentiment', models.BooleanField()),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('address', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
