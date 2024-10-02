from django.urls import path  # path nos permite crear las urls que necesitemos
from . import views  # me traigo todas las vistas

## from django.contrib.auth import views as auth_views  # Importa las vistas de autenticación

app_name = "namespaceusers"

urlpatterns = [
    path("", views.viewLogin, name="login"),
]
