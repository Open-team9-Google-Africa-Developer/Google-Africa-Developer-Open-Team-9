from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(verbose_name=_("Category Name"), help_text=_("Required"), max_length=255, unique=True)
    slug = models.SlugField(verbose_name=_("Category Safe URL"), max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        return reverse("complaint:category", args=[self.slug])

    def __str__(self):
        return self.name


class Crime(models.Model):

    options = (("minor", "Minor"), ("major", "Major"))

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(verbose_name=_("Crime Name"), help_text=_("Required"), max_length=100)
    severity = models.CharField(max_length=100, choices=options, default="minor")

    class Meta:
        verbose_name = _("Crime")
        verbose_name_plural = _("Crimes")

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
    complainant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="complaints")
    status = models.CharField(max_length=100, choices=options, default="pending")
    created_at = models.DateTimeField(_("Created at"), default=timezone.now)
    updated_at = models.DateTimeField(_("Created at"), default=timezone.now)
    slug = models.SlugField(max_length=250, unique_for_date="created_at")
    objects = models.Manager()
    complaintobjects = ComplaintObjects()  # Custom Model Manager

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Complaint")
        verbose_name_plural = _("Complaints")

    def get_absolute_url(self):
        return reverse("complaint:complaint_detail", args=[self.slug])

    def __str__(self):
        return self.title


class ComplaintImage(models.Model):
    """The Complaint Image Table"""

    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, related_name="complaint_image")
    image = models.ImageField(
        _("image"), upload_to="images/", height_field=None, width_field=None, default="images/default.png"
    )
    alt_text = models.CharField(verbose_name=_("Alternative Text"), max_length=255, null=True, blank=True)
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(_("Created at"), default=timezone.now)
    updated_at = models.DateTimeField(_("Created at"), default=timezone.now)

    class Meta:

        verbose_name = _("Complaint Image")
        verbose_name_plural = _("Complaint Images")
