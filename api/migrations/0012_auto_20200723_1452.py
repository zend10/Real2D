# Generated by Django 3.0.7 on 2020-07-23 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20200723_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='alt_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='alt_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]