from django.contrib import admin
from .models import Entrantes, Principales, Postre, Bebida, Precio
from django.utils.text import Truncator


class BaseMenuItemAdmin(admin.ModelAdmin):
    list_display = ["titulo", "truncated_descripcion", "fecha_alta"]
    list_filter = ["titulo"]
    max_items = 5  # Define el límite máximo aquí para que sea reutilizable

    def truncated_descripcion(self, obj):
        return Truncator(obj.descripcion).chars(50) # Muestra solo los primeros 50 caracteres

    truncated_descripcion.short_description = "Descripción" # Renombra la columna

    def has_add_permission(self, request):
        # Lógica reutilizable para limitar los elementos
        if self.model.objects.count() >= self.max_items:
            return False  # No permitirá agregar más, desactiva el botón de agregar
        return True

    # Añadir el archivo JS personalizado usando la clase Media
    # class Media:
    # js = ("js/admin_custom.js",)  # Ruta relativa dentro de la carpeta /static


# Registramos cada clase utilizando la clase base
@admin.register(Entrantes)
class EntrantesAdmin(BaseMenuItemAdmin):
    pass


@admin.register(Principales)
class PrincipalesAdmin(BaseMenuItemAdmin):
    pass


@admin.register(Postre)
class PostreAdmin(BaseMenuItemAdmin):
    pass


@admin.register(Bebida)
class BebidaAdmin(BaseMenuItemAdmin):
    pass


@admin.register(Precio)
class PrecioAdmin(admin.ModelAdmin):
    list_display = ["precio", "fecha_alta"]
    
    def has_add_permission(self, request):
        max_items = 1
        if Precio.objects.count() >= max_items:
            return False
        return True
