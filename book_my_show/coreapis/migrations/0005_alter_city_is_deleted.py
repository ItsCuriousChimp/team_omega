# Generated by Django 4.0.5 on 2022-07-26 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapis', '0004_remove_booking_deleted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='is_deleted',
            field=models.BooleanField(default=True),
        ),
    ]