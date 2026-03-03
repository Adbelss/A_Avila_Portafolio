from django.contrib import admin
from .models import Project, Technology


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
	list_display = ("name", "slug")
	search_fields = ("name",)
	prepopulated_fields = {"slug": ("name",)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ("title", "is_featured", "created_at")
	list_filter = ("is_featured", "created_at")
	search_fields = ("title", "short_description", "description")
	prepopulated_fields = {"slug": ("title",)}
	filter_horizontal = ("technologies",)
