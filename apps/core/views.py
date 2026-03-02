from django.shortcuts import render


def home(request):
    """
    Home principal del portafolio.
    """
    return render(request, "core/home.html")