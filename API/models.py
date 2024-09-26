from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class MenuItemBase(models.Model):
    titulo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=100)
    fecha_alta = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True  # Esto indica que no se creará una tabla para este modelo


class Entrantes(MenuItemBase):
    pass
    """ Comentado en caso se necesite una validación global """
    # def save(self, *args, **kwargs):
    #     max_items = 5
    #     if Entrantes.objects.count() >= max_items:
    #         raise ValidationError(
    #             f"Ya existen {max_items} entrantes. Contante con su programador para actualizarlo."
    #         )
    #     super().save(*args, **kwargs)


class Principales(MenuItemBase):
    pass


class Postre(MenuItemBase):
    pass


class Bebida(MenuItemBase):
    pass


class Precio(models.Model):
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_alta = models.DateTimeField(auto_now_add=True)
