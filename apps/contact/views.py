from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .forms import ContactForm


@require_http_methods(["GET", "POST"])
def contact_view(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			lead = form.save(commit=False)
			lead.source = "web"
			lead.save()

			messages.success(
				request,
				"Solicitud enviada correctamente. Te contactaré lo antes posible.",
			)
			return redirect("contact:contact")
		messages.error(request, "Revisa el formulario e inténtalo de nuevo.")
	else:
		form = ContactForm()

	return render(request, "contact/contact.html", {"form": form})
