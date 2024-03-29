# Generated by Django 4.1.3 on 2022-12-18 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                (
                    "name",
                    models.CharField(
                        help_text="Required",
                        max_length=255,
                        unique=True,
                        verbose_name="Category Name",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=255, unique=True, verbose_name="Category Safe URL"
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Complaint",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("location", models.CharField(max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("investigating", "Investigating"),
                            ("solved", "Solved"),
                        ],
                        default="pending",
                        max_length=100,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Created at"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Created at"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(max_length=250, unique_for_date="created_at"),
                ),
                (
                    "complainant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="complaints",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Complaint",
                "verbose_name_plural": "Complaints",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="Crime",
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
                (
                    "name",
                    models.CharField(
                        help_text="Required", max_length=100, verbose_name="Crime Name"
                    ),
                ),
                (
                    "severity",
                    models.CharField(
                        choices=[("minor", "Minor"), ("major", "Major")],
                        default="minor",
                        max_length=100,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="complaint.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Crime",
                "verbose_name_plural": "Crimes",
            },
        ),
        migrations.CreateModel(
            name="ComplaintImage",
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
                (
                    "image",
                    models.ImageField(
                        default="images/default.png",
                        upload_to="images/",
                        verbose_name="image",
                    ),
                ),
                (
                    "alt_text",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Alternative Text",
                    ),
                ),
                ("is_feature", models.BooleanField(default=False)),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Created at"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Created at"
                    ),
                ),
                (
                    "complaint",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="complaint_image",
                        to="complaint.complaint",
                    ),
                ),
            ],
            options={
                "verbose_name": "Complaint Image",
                "verbose_name_plural": "Complaint Images",
            },
        ),
        migrations.AddField(
            model_name="complaint",
            name="crime",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="complaint.crime"
            ),
        ),
    ]
