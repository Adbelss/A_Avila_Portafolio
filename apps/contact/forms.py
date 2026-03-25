from django import forms

from .models import Lead


class ContactForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Tu nombre completo",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "tu_correo@ejemplo.com",
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Asunto del mensaje",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Escribe aquí tu mensaje",
                    "rows": 6,
                }
            ),
        }
