from django.shortcuts import render


def index(request):
    context = {"site_key": "6LeY1fklAAAAAL3E6jKd2TTYomhvdLxXLfRlm243"}

    return render(request, "recaptcha/index.html", context)
