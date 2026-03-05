from django.db import models
from django.utils.text import slugify


class ProjectQuerySet(models.QuerySet):
	def published(self):
		return self.filter(status=self.model.Status.PUBLISHED)

	def featured(self):
		return self.published().filter(is_featured=True)

	def with_related(self):
		return self.prefetch_related("technologies", "images")


class TechnologyQuerySet(models.QuerySet):
	def ordered(self):
		return self.order_by("order", "name")


class Project(models.Model):
	class Status(models.TextChoices):
		DRAFT = "draft", "Borrador"
		PUBLISHED = "published", "Publicado"

	title = models.CharField(max_length=160)
	slug = models.SlugField(max_length=180, blank=True)
	summary = models.CharField(max_length=280, blank=True)

	# campos previos preservados (si tenías campos extra no los borré)
	short_description = models.CharField(max_length=220, blank=True)
	description = models.TextField(blank=True)

	problem = models.TextField(blank=True)
	solution = models.TextField(blank=True)
	responsibilities = models.TextField(blank=True)
	stack_summary = models.CharField(max_length=240, blank=True)

	status = models.CharField(
		max_length=16,
		choices=Status.choices,
		default=Status.DRAFT,
		db_index=True,
	)

	start_date = models.DateField(blank=True, null=True)
	end_date = models.DateField(blank=True, null=True)

	is_featured = models.BooleanField(default=False, db_index=True)
	order = models.PositiveIntegerField(default=0, db_index=True)

	github_url = models.URLField(blank=True)
	demo_url = models.URLField(blank=True)

	technologies = models.ManyToManyField(
		"Technology",
		related_name="projects",
		blank=True,
	)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = ProjectQuerySet.as_manager()

	class Meta:
		ordering = ["order", "-created_at"]
		constraints = [
			models.UniqueConstraint(fields=["slug"], name="uq_project_slug"),
		]
		indexes = [
			models.Index(fields=["status", "is_featured"], name="idx_project_status_feat"),
			models.Index(fields=["order", "created_at"], name="idx_project_order_created"),
		]

	def __str__(self) -> str:
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)[:180]
		super().save(*args, **kwargs)



class ProjectImage(models.Model):
	project = models.ForeignKey(
		Project,
		on_delete=models.CASCADE,
		related_name="images",
	)
	image = models.ImageField(upload_to="projects/")
	alt_text = models.CharField(max_length=160, blank=True)
	order = models.PositiveIntegerField(default=0, db_index=True)

	class Meta:
		ordering = ["order", "id"]
		indexes = [
			models.Index(fields=["project", "order"], name="idx_projectimage_proj_order"),
		]

	def __str__(self) -> str:
		return f"{self.project.title} - {self.order}"



class Technology(models.Model):
	class Category(models.TextChoices):
		BACKEND = "backend", "Backend"
		FRONTEND = "frontend", "Frontend"
		DATABASE = "db", "Base de datos"
		DEVOPS = "devops", "DevOps"
		OTHER = "other", "Otros"

	name = models.CharField(max_length=80)
	slug = models.SlugField(max_length=90, blank=True)
	category = models.CharField(
		max_length=16,
		choices=Category.choices,
		default=Category.OTHER,
		db_index=True,
	)
	icon = models.CharField(max_length=120, blank=True)
	order = models.PositiveIntegerField(default=0, db_index=True)

	objects = TechnologyQuerySet.as_manager()

	class Meta:
		ordering = ["order", "name"]
		constraints = [
			models.UniqueConstraint(fields=["slug"], name="uq_technology_slug"),
		]
		indexes = [
			models.Index(fields=["category", "order"], name="idx_tech_category_order"),
		]

	def __str__(self) -> str:
		return self.name

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)[:90]
		super().save(*args, **kwargs)
