from django.conf import settings


def global_contact_settings(_request):
    return {
        "WHATSAPP_PHONE_E164": getattr(settings, "WHATSAPP_PHONE_E164", ""),
        "WHATSAPP_DEFAULT_TEXT": getattr(settings, "WHATSAPP_DEFAULT_TEXT", ""),
    }
