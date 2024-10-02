from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.http import JsonResponse

# OBLIGATORIO, si queremos que se registre en la DB de la tabla de usuario
from .models import User


def viewLogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # Verificar si el usuario es un superusuario
            if user.is_superuser:
                return JsonResponse(
                    {"redirect": "/admin/"}
                )  # / => pag inicial
            else:
                return JsonResponse(
                    {"redirect": "/admin/"} 
                )  # login
        else:
            return JsonResponse({"error": "Credenciales inválidas"}, status=400)
