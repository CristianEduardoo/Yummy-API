from rest_framework import serializers # Se encargan de convertir la información de los modelos a JSON
from .models import Entrantes, Principales, Postre, Bebida, Precio


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = None  # Útil para dejar claro que los modelos hijos lo definirán
        fields = ("id", "titulo", "descripcion", "fecha_alta")


class EntrantesSerializer(MenuItemSerializer):
    class Meta(MenuItemSerializer.Meta):
        model = Entrantes


class PrincipalesSerializer(MenuItemSerializer):
    class Meta(MenuItemSerializer.Meta):
        model = Principales


class PostreSerializer(MenuItemSerializer):
    class Meta(MenuItemSerializer.Meta):
        model = Postre


class BebidaSerializer(MenuItemSerializer):
    class Meta(MenuItemSerializer.Meta):
        model = Bebida


class PrecioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precio
        fields = ("id", "precio", "fecha_alta")
