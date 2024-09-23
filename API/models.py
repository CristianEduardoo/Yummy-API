from django.db import models

# Create your models here.

class MenuItemBase(models.Model):
    titulo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=260)
    fecha_alta = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True  # Esto indica que no se creará una tabla para este modelo


class Entrantes(MenuItemBase):
    pass


class Principales(MenuItemBase):
    pass


class Postre(MenuItemBase):
    pass


class Bebida(MenuItemBase):
    pass


class Precio(models.Model):
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_alta = models.DateTimeField(auto_now_add=True)
