from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Crime(models.Model):

    options = (("minor", "Minor"), ("major", "Major"))

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    severity = models.CharField(max_length=100, choices=options, default="minor")

    def __str__(self):
        return self.name


class Complaint(models.Model):
    class ComplaintObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="pending")

    options = (
        ("pending", "Pending"),
        ("investigating", "Investigating"),
        ("solved", "Solved"),
    )

    crime = models.ForeignKey(Crime, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=255)
    complainant = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="complaints"
    )
    status = models.CharField(max_length=100, choices=options, default="pending")
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=250, unique_for_date="created_at")
    objects = models.Manager()
    complaintobjects = ComplaintObjects()  # Custom Model Manager

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
