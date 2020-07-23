# Generated by Django 3.0.7 on 2020-07-23 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20200713_0520'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='alt_name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='source',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='series',
            name='alt_name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='series',
            name='source',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]