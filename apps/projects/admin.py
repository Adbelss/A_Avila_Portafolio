
from django.contrib import admin
from django.utils.html import format_html

from .models import Project, ProjectImage, Technology


class ProjectImageInline(admin.TabularInline):
	model = ProjectImage
	extra = 0
	fields = ("preview", "image", "alt_text", "order")
	readonly_fields = ("preview",)
	ordering = ("order", "id")

	def preview(self, obj):
		if obj and obj.image:
			return format_html(
				'<img src="{}" style="height:48px;width:auto;border-radius:6px;" />',
				obj.image.url,
			)
		return "-"

	preview.short_description = "Vista previa"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = (
		"created_at",
		"title",
		"status",
		"is_featured",
		"order",
		"github_url",
		"demo_url",
	)
	list_filter = ("status", "is_featured", "created_at")
	search_fields = ("title", "summary", "stack_summary", "problem", "solution")
	ordering = ("order", "-created_at")
	date_hierarchy = "created_at"

	prepopulated_fields = {"slug": ("title",)}
	list_editable = ("status", "is_featured", "order")

	inlines = (ProjectImageInline,)

	filter_horizontal = ()
	autocomplete_fields = ("technologies",)

	fieldsets = (
		("Información principal", {
			"fields": ("title", "slug", "summary", "status", "is_featured", "order"),
		}),
		("Contenido", {
			"fields": ("problem", "solution", "responsibilities", "stack_summary"),
		}),
		("Fechas", {
			"fields": ("start_date", "end_date"),
		}),
		("Enlaces", {
			"fields": ("github_url", "demo_url"),
		}),
		("Tecnologías", {
			"fields": ("technologies",),
		}),
		("Sistema", {
			"fields": ("created_at", "updated_at"),
		}),
	)
	readonly_fields = ("created_at", "updated_at")

	actions = ("mark_published", "mark_draft", "set_featured", "unset_featured")

	@admin.action(description="Publicar seleccionados")
	def mark_published(self, request, queryset):
		queryset.update(status=Project.Status.PUBLISHED)

	@admin.action(description="Marcar como borrador")
	def mark_draft(self, request, queryset):
		queryset.update(status=Project.Status.DRAFT)

	@admin.action(description="Marcar como destacados")
	def set_featured(self, request, queryset):
		queryset.update(is_featured=True)

	@admin.action(description="Quitar destacados")
	def unset_featured(self, request, queryset):
		queryset.update(is_featured=False)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
	list_display = ("name", "category", "order", "slug")
	list_filter = ("category",)
	search_fields = ("name", "slug")
	ordering = ("order", "name")
	list_editable = ("category", "order")
	prepopulated_fields = {"slug": ("name",)}

	fieldsets = (
		("Datos", {"fields": ("name", "slug", "category", "icon", "order")} ),
	)
