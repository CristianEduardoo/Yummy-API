from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

""" PARA ACCEDER A LOS ESQUEMAS CREADOS archivo.yml desde la web, tenemos que establecer las url's """
from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")), # URL de Autenticacion y Autorización de Django
    
    # Ruta que redirige a login como la página principal
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False), name='login_redirect'),

    # Rutas para la API
    path('api/v1/', include('API.urls', namespace="api_restful")),
    
    # Rutas para la documentación de la API generada con drf_spectacular
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),  # Genera el archivo YAML
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),  # Swagger UI
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),  # ReDoc UI
]
