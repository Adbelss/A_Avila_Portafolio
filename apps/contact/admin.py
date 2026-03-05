from django.contrib import admin
from django.utils.html import format_html

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
	list_display = ("created_at", "name", "email", "phone", "source", "status_badge")
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
	def mark_as_read(self, request, queryset):
		queryset.update(is_read=True)

	@admin.action(description="Marcar como no leído")
	def mark_as_unread(self, request, queryset):
		queryset.update(is_read=False)

	def status_badge(self, obj):
		if obj.is_read:
			return format_html('<span style="padding:2px 8px;border-radius:999px;background:#1f6f43;color:#fff;">Leído</span>')
		return format_html('<span style="padding:2px 8px;border-radius:999px;background:#9b1c1c;color:#fff;">Nuevo</span>')

	status_badge.short_description = "Estado"

	def change_view(self, request, object_id, form_url="", extra_context=None):
		obj = self.get_object(request, object_id)
		if obj and not obj.is_read:
			obj.is_read = True
			obj.save(update_fields=["is_read"])
		return super().change_view(request, object_id, form_url, extra_context)
