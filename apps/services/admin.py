from django.contrib import admin

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ("name", "is_active", "order", "slug", "created_at")
	list_filter = ("is_active", "created_at")
	search_fields = ("name", "description", "deliverables", "price_hint")
	ordering = ("order", "name")
	date_hierarchy = "created_at"

	prepopulated_fields = {"slug": ("name",)}
	list_editable = ("is_active", "order")

	fieldsets = (
		("Información", {"fields": ("name", "slug", "is_active", "order")} ),
		("Contenido", {"fields": ("description", "deliverables", "price_hint")} ),
		("Sistema", {"fields": ("created_at",)} ),
	)
	readonly_fields = ("created_at",)

	actions = ("activate_services", "deactivate_services")

	@admin.action(description="Activar seleccionados")
	def activate_services(self, request, queryset):
		queryset.update(is_active=True)

	@admin.action(description="Desactivar seleccionados")
	def deactivate_services(self, request, queryset):
		queryset.update(is_active=False)
