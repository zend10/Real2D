# Generated by Django 3.0.7 on 2020-06-08 10:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200607_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationimage',
            name='image_name',
            field=models.UUIDField(default=uuid.UUID('6cc464b2-83a3-403a-9ecb-77833dd7a907'), editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='image_name',
            field=models.UUIDField(default=uuid.UUID('b70422bc-8c91-4f59-b33f-f8991d067476'), editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='serieslocationimage',
            name='image_name',
            field=models.UUIDField(default=uuid.UUID('d534fb98-a754-4c11-85fb-c6c6b42f0ff0'), editable=False, unique=True),
        ),
    ]
