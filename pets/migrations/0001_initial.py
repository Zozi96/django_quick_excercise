# Generated by Django 4.1.7 on 2023-03-08 02:40

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pet",
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
                ("name", models.CharField(max_length=100)),
                ("date_of_birth", models.DateField()),
                (
                    "breed",
                    models.CharField(
                        choices=[("Dog", "Dog")], default="Dog", max_length=20
                    ),
                ),
                ("gender", models.CharField(max_length=10)),
                ("weight", models.DecimalField(decimal_places=2, max_digits=5)),
                ("deceased_date", models.DateField(blank=True, null=True)),
            ],
        ),
    ]
