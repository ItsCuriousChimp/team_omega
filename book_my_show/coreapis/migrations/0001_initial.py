# Generated by Django 4.0.5 on 2022-07-12 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Cinema",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deleted", models.DateTimeField(editable=False, null=True)),
                (
                    "deleted_by_cascade",
                    models.BooleanField(default=False, editable=False),
                ),
                ("created_at_utc", models.DateTimeField(auto_now_add=True)),
                ("modified_at_utc", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=32)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CinemaScreen",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deleted", models.DateTimeField(editable=False, null=True)),
                (
                    "deleted_by_cascade",
                    models.BooleanField(default=False, editable=False),
                ),
                ("created_at_utc", models.DateTimeField(auto_now_add=True)),
                ("modified_at_utc", models.DateTimeField(auto_now=True)),
                ("screen_no", models.IntegerField()),
                (
                    "cinema_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="coreapis.cinema",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deleted", models.DateTimeField(editable=False, null=True)),
                (
                    "deleted_by_cascade",
                    models.BooleanField(default=False, editable=False),
                ),
                ("created_at_utc", models.DateTimeField(auto_now_add=True)),
                ("modified_at_utc", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=32)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deleted", models.DateTimeField(editable=False, null=True)),
                (
                    "deleted_by_cascade",
                    models.BooleanField(default=False, editable=False),
                ),
                ("created_at_utc", models.DateTimeField(auto_now_add=True)),
                ("modified_at_utc", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=32)),
                ("description", models.TextField()),
                ("release_date", models.DateField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Showtime",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deleted", models.DateTimeField(editable=False, null=True)),
                (
                    "deleted_by_cascade",
                    models.BooleanField(default=False, editable=False),
                ),
                ("created_at_utc", models.DateTimeField(auto_now_add=True)),
                ("modified_at_utc", models.DateTimeField(auto_now=True)),
                ("start_time_at_utc", models.DateTimeField()),
                ("end_time_at_utc", models.DateTimeField()),
                (
                    "cinema_screen_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="coreapis.cinemascreen",
                    ),
                ),
                (
                    "movie_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="coreapis.movie"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Seat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deleted", models.DateTimeField(editable=False, null=True)),
                (
                    "deleted_by_cascade",
                    models.BooleanField(default=False, editable=False),
                ),
                ("created_at_utc", models.DateTimeField(auto_now_add=True)),
                ("modified_at_utc", models.DateTimeField(auto_now=True)),
                ("seat_no", models.CharField(max_length=8)),
                (
                    "cinema_screen_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="coreapis.cinemascreen",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="cinema",
            name="city_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="coreapis.city"
            ),
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deleted", models.DateTimeField(editable=False, null=True)),
                (
                    "deleted_by_cascade",
                    models.BooleanField(default=False, editable=False),
                ),
                ("created_at_utc", models.DateTimeField(auto_now_add=True)),
                ("modified_at_utc", models.DateTimeField(auto_now=True)),
                (
                    "seat_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="coreapis.seat"
                    ),
                ),
                (
                    "show_time_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="coreapis.showtime",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
