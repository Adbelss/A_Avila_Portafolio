from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import ContactForm


class ContactView(FormView):
    template_name = "contact/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact:contact")

    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.source = "web"
        lead.save()

        messages.success(
            self.request,
            "Solicitud enviada correctamente. Te contactaré lo antes posible.",
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Revisa el formulario e inténtalo de nuevo.")
        return super().form_invalid(form)
