# Nos olvidamos del render y usamos un viewsets y permissions
from rest_framework import viewsets, permissions
from .models import Entrantes, Principales, Postre, Bebida, Precio
from .serializers import EntrantesSerializer, PrincipalesSerializer, PostreSerializer, BebidaSerializer, PrecioSerializer

# Create your viewsets here.

class MenuItemViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EntrantesViewSet(MenuItemViewSet):
    queryset = Entrantes.objects.all() # queryset => es convención. Le decimos que nos traiga todos Entrantes
    serializer_class = EntrantesSerializer # Le decimos que serializador va a usar

class PrincipalesViewSet(MenuItemViewSet):
    queryset = Principales.objects.all()
    serializer_class = PrincipalesSerializer

class PostreViewSet(MenuItemViewSet):
    queryset = Postre.objects.all()
    serializer_class = PostreSerializer

class BebidaViewSet(MenuItemViewSet):
    queryset = Bebida.objects.all()
    serializer_class = BebidaSerializer

class PrecioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Precio.objects.all()
    serializer_class = PrecioSerializer
