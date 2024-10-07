from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView


# Sobrescribir la URL de login del admin
admin.site.login = auth_views.LoginView.as_view(template_name='registration/login.html')

""" PARA ACCEDER A LOS ESQUEMAS CREADOS archivo.yml desde la web, tenemos que establecer las url's """
from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path("accounts/", include("django.contrib.auth.urls")), # URL de Autenticacion y Autorización de Django
    
    # Ruta que redirige a login como la página principal
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False), name='login_redirect'),
    path("login-user/", include("Users.urls", namespace="login-user")),

    # Rutas para la API
    path('api/v1/', include('API.urls', namespace="api_restful")),
    
    # Rutas para la documentación de la API generada con drf_spectacular
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),  # Genera el archivo YAML
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),  # Swagger UI
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),  # ReDoc UI
]
