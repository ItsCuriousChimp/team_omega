# Generated by Django 4.0.5 on 2022-07-11 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("coreapis", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="seat",
            old_name="cinems_screen_id",
            new_name="cinema_screen_id",
        ),
    ]
