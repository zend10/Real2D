# Generated by Django 3.0.7 on 2020-06-06 18:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('remarks', models.TextField(blank=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('last_modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(null=True, upload_to='cover')),
                ('image_name', models.UUIDField(default=uuid.UUID('750da74b-0cf5-49b1-9d4b-459d898b3329'), editable=False, unique=True)),
                ('description', models.TextField()),
                ('anilist_id', models.IntegerField()),
                ('last_modified', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Series',
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.CreateModel(
            name='SeriesLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.TextField(blank=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Location')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Series')),
            ],
        ),
    ]
