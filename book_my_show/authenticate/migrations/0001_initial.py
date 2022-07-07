from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserModel",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "email",
                    models.EmailField(max_length=60, unique=True, verbose_name="email"),
                ),
                (
                    "last_login",
                    models.DateTimeField(auto_now=True, verbose_name="last login"),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=100)),
                ("phone_no", models.CharField(max_length=15)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
