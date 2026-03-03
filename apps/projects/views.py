from django.shortcuts import render, get_object_or_404
from .models import Project


def project_list(request):
	"""
	Listado de proyectos.
	"""
	projects = (
		Project.objects
		.prefetch_related("technologies")
		.all()
	)

	return render(request, "projects/project_list.html", {
		"projects": projects
	})


def project_detail(request, slug):
	"""
	Detalle de proyecto.
	"""
	project = get_object_or_404(
		Project.objects.prefetch_related("technologies"),
		slug=slug
	)

	return render(request, "projects/project_detail.html", {
		"project": project
	})
