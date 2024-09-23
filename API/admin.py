from django.contrib import admin
from .models import Entrantes, Principales, Postre, Bebida
from django.utils.text import Truncator


# Decoradores para manejar mejor la UI del Admin en la web
@admin.register(Entrantes)
class EntrantesAdmin(admin.ModelAdmin):
    list_display = ["titulo", "descripcion", "fecha_alta"]
    list_filter = ["titulo"]

    class Meta:
        verbose_name_plural = "Entrante"
