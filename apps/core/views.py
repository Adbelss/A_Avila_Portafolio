from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["service_web"] = {
            "name": "Desarrollo Web Profesional",
            "description": "Creación de sitios y sistemas web con estructura limpia, diseño profesional y enfoque en mantenibilidad.",
        }
        context["service_db"] = {
            "name": "Bases de Datos",
            "description": "Diseño, organización y mejora de bases de datos para proyectos que requieren orden, estabilidad y crecimiento.",
        }
        context["service_auto"] = {
            "name": "Automatización de Procesos",
            "description": "Automatización de tareas repetitivas para optimizar tiempo, flujo de trabajo y productividad.",
        }

        context["project_one"] = {
            "title": "Sistema Web Empresarial",
            "summary": "Desarrollo de una solución administrativa web con estructura modular y enfoque profesional.",
        }
        context["project_two"] = {
            "title": "Portafolio Profesional Django",
            "summary": "Construcción de un portafolio web escalable, limpio y orientado a presentación profesional.",
        }
        context["project_three"] = {
            "title": "Automatización de Gestión",
            "summary": "Implementación de procesos automatizados para mejorar control, seguimiento y eficiencia operativa.",
        }

        return context


class AboutView(TemplateView):
    template_name = "core/about.html"
