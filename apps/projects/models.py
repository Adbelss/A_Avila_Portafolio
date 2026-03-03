from django.db import models
from django.utils.text import slugify


class Technology(models.Model):
	"""
	Tecnología usada en proyectos (ej. Django, MySQL, Bootstrap).
	"""
	name = models.CharField(max_length=80, unique=True)
	slug = models.SlugField(max_length=90, unique=True, blank=True)

	class Meta:
		verbose_name = "Tecnología"
		verbose_name_plural = "Tecnologías"
		ordering = ["name"]

	def save(self, *args, **kwargs):
		if not self.slug:
			base = slugify(self.name)
			slug = base
			i = 2
			while Technology.objects.filter(slug=slug).exclude(pk=self.pk).exists():
				slug = f"{base}-{i}"
				i += 1
			self.slug = slug
		super().save(*args, **kwargs)

	def __str__(self) -> str:
		return self.name


class Project(models.Model):
	"""
	Proyecto/caso de estudio del portafolio.
	"""
	title = models.CharField(max_length=150)
	slug = models.SlugField(max_length=170, unique=True, blank=True)

	short_description = models.CharField(max_length=220)
	description = models.TextField()

	technologies = models.ManyToManyField(
		Technology,
		blank=True,
		related_name="projects",
	)

	is_featured = models.BooleanField(default=False)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Proyecto"
		verbose_name_plural = "Proyectos"
		ordering = ["-is_featured", "-created_at"]

	def save(self, *args, **kwargs):
		if not self.slug:
			base = slugify(self.title)
			slug = base
			i = 2
			while Project.objects.filter(slug=slug).exclude(pk=self.pk).exists():
				slug = f"{base}-{i}"
				i += 1
			self.slug = slug
		super().save(*args, **kwargs)

	def __str__(self) -> str:
		return self.title
