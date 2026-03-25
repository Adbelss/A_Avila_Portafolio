from django.urls import path

from apps.services.views import ServiceListView

app_name = "services"

urlpatterns = [
    path("", ServiceListView.as_view(), name="service_list"),
]
