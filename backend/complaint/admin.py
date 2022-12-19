from django.contrib import admin

from . import models


class ComplaintImageInline(admin.TabularInline):
    model = models.ComplaintImage


@admin.register(models.Complaint)
class ComplainantAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "crime", "complainant", "status")
    inlines = [ComplaintImageInline]
    prepopulated_fields = {
        "slug": ("title",),
    }


admin.site.register(models.Category)

admin.site.register(models.Crime)
# admin.site.register(models.ComplaintImage)
