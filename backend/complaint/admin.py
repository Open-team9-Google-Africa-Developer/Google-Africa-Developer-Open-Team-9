from django.contrib import admin
from . import models


@admin.register(models.Complaint)
class ComplainantAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "crime", "complainant", "status")
    prepopulated_fields = {
        "slug": ("title",),
    }


admin.site.register(models.Category)

admin.site.register(models.Crime)
