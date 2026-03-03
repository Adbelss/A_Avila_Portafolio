from django.shortcuts import render
from apps.projects.models import Project


def home(request):
    """
    Home principal del portafolio.
    """
    featured_projects = (
        Project.objects
        .filter(is_featured=True)
        .prefetch_related("technologies")
        .order_by("-created_at")[:3]
    )

    return render(request, "core/home.html", {
        "featured_projects": featured_projects
    })