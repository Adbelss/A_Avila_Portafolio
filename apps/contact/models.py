from django.core.validators import RegexValidator
from django.db import models


class Lead(models.Model):
	"""Modelo que representa un lead/contacto enviado desde el sitio web."""

	name = models.CharField(max_length=120)
	email = models.EmailField(max_length=254)
	phone = models.CharField(
		max_length=30,
		blank=True,
		validators=[
			RegexValidator(
				regex=r"^[0-9+\-() ]{7,30}$",
				message="Ingresa un teléfono válido.",
			)
		],
	)
	message = models.TextField(max_length=2000)
	source = models.CharField(max_length=50, blank=True, default="web")

	created_at = models.DateTimeField(auto_now_add=True)

	is_read = models.BooleanField(default=False)
	notes = models.TextField(blank=True)

	class Meta:
		ordering = ["-created_at"]
		indexes = [
			models.Index(fields=["created_at"]),
			models.Index(fields=["is_read"]),
			models.Index(fields=["source"]),
		]

	def __str__(self) -> str:
		return f"{self.name} - {self.email}"
