# Generated by Django 4.2.2 on 2023-07-25 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=25)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.IntegerField()),
                ("date", models.DateField()),
                ("gender", models.CharField(max_length=25)),
                ("event", models.CharField(max_length=50)),
                ("location", models.CharField(max_length=50)),
            ],
        ),
    ]
