from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularSwaggerView,
    SpectacularRedocView,
    SpectacularAPIView,
)
import os
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger/",
        # csrf_exempt(CustomSwaggerView.as_view()),
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-view",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc-view",
    ),
    # apps url
    path("auth/", include("identity.urls")),
]

if (
    os.environ.get("DJANGO_SETTINGS_MODULE", "core.settings.local")
    == "core.settings.local"
):
    urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
