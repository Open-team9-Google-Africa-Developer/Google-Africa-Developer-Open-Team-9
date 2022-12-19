from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("complaint.urls", namespace="complaint")),
    path("api/", include("complaint_api.urls", namespace="complaint_api")),
    path("api/account/", include("account.api.urls", namespace="account_api")),
    path("account/", include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
