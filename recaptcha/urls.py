from django.urls import path

from . import views

app_name = "recaptcha"

urlpatterns = [
    path("index/", views.index, name="index"),
]
