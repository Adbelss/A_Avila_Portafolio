from django.urls import path

from apps.core.views import AboutView, HomeView

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("sobre-mi/", AboutView.as_view(), name="about"),
]
