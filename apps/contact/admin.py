from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
	list_display = ("created_at", "name", "email", "phone", "source", "is_read")
	list_filter = ("is_read", "source", "created_at")
	search_fields = ("name", "email", "phone", "message")
	ordering = ("-created_at",)
	readonly_fields = ("created_at",)

	fieldsets = (
		("Datos del lead", {"fields": ("name", "email", "phone", "message", "source")} ),
		("Seguimiento interno", {"fields": ("is_read", "notes", "created_at")} ),
	)

	actions = ("mark_as_read", "mark_as_unread")

	@admin.action(description="Marcar como leído")
	def mark_as_read(self, _request, queryset):
		queryset.update(is_read=True)

	@admin.action(description="Marcar como no leído")
	def mark_as_unread(self, _request, queryset):
		queryset.update(is_read=False)
