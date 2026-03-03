from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),
    path("proyectos/", include("apps.projects.urls")),
    path("contacto/", include("apps.contact.urls")),
]