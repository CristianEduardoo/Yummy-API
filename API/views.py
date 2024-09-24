# Nos olvidamos del render y usamos un viewsets y permissions
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Entrantes, Principales, Postre, Bebida, Precio
from .serializers import EntrantesSerializer, PrincipalesSerializer, PostreSerializer, BebidaSerializer, PrecioSerializer

# Create your viewsets here.

class MenuItemViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Método para validación personalizada en la creación de un nuevo objeto
    def create(self, request, *args, **kwargs):
        model_class = self.get_queryset().model # Obtiene el modelo actual (Entrantes, Principales, etc.)
        max_items = 5  # Límite máximo de elementos
        current_count = model_class.objects.count()

        if current_count >= max_items:
            return Response(
                {
                    "error": f"Se ha alcanzado el límite máximo de {max_items} {model_class._meta.verbose_name_plural}."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().create(request, *args, **kwargs)


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
