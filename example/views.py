from django.conf import settings
from django.shortcuts import render


def index(request):
    return render(request, "index.html", {"GOOGLE_CLIENT_ID": settings.SOCIAL_AUTH_GOOGLE_ONETAP_KEY})
