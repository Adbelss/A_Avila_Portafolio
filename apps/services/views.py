from django.views.generic import TemplateView


class ServiceListView(TemplateView):
    template_name = "services/service_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = [
            {
                "name": "Desarrollo Web Profesional",
                "description": "Desarrollo de páginas y sistemas web con Django, estructura clara y diseño profesional.",
            },
            {
                "name": "Implementación de Sistemas",
                "description": "Construcción de soluciones funcionales para procesos internos, gestión de información y operación diaria.",
            },
            {
                "name": "Diseño y Organización de Bases de Datos",
                "description": "Estructuración de datos con enfoque en integridad, crecimiento y facilidad de mantenimiento.",
            },
            {
                "name": "Automatización de Tareas",
                "description": "Automatización de procesos manuales para mejorar productividad y reducir errores repetitivos.",
            },
            {
                "name": "Mantenimiento y Mejora de Proyectos",
                "description": "Optimización de proyectos existentes, corrección de estructura y fortalecimiento técnico.",
            },
            {
                "name": "Asesoría Técnica",
                "description": "Apoyo en planificación, estructura y definición técnica para proyectos web y tecnológicos.",
            },
        ]
        return context
