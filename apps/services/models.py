from django.db import models
# Create your models here.
from django.utils.text import slugify

class ServiceQuerySet(models.QuerySet):
	def active(self):
		return self.filter(is_active=True).order_by("order", "name")

class Service(models.Model):
	name = models.CharField(max_length=120)
	slug = models.SlugField(max_length=140)

	description = models.TextField()
	deliverables = models.TextField(blank=True)
	price_hint = models.CharField(max_length=120, blank=True)

	order = models.PositiveIntegerField(default=0, db_index=True)
	is_active = models.BooleanField(default=True, db_index=True)

	created_at = models.DateTimeField(auto_now_add=True)

	objects = ServiceQuerySet.as_manager()

	class Meta:
		ordering = ["order", "name"]
		constraints = [
			models.UniqueConstraint(fields=["slug"], name="uq_service_slug"),
		]
		indexes = [
			models.Index(fields=["is_active", "order"], name="idx_service_active_order"),
		]

	def __str__(self) -> str:
		return self.name

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)[:140]
		super().save(*args, **kwargs)
# Create your models here.
