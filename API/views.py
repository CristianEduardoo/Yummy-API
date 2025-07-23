from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
# from rest_framework.views import APIView
from django.http import JsonResponse
from .models import Entrantes, Principales, Postre, Bebida, Precio
from .serializers import EntrantesSerializer, PrincipalesSerializer, PostreSerializer, BebidaSerializer, PrecioSerializer

# ViewSet base para manejar las restricciones de creación de ítems
class MenuItemViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # http_method_names = ["get"]  # Solo se permiten solicitudes GET

    # Método para validación personalizada en la creación de un nuevo objeto
    def create(self, request, *args, **kwargs):
        model_class = self.get_queryset().model  # Obtiene el modelo actual (Entrantes, Principales, etc.)
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

# ViewSets para cada tipo de ítem
class EntrantesViewSet(MenuItemViewSet):
    queryset = Entrantes.objects.all() # queryset => es convención. Le decimos que nos traiga todos Entrantes
    serializer_class = EntrantesSerializer  # Le decimos que serializador va a usar

class PrincipalesViewSet(MenuItemViewSet):
    queryset = Principales.objects.all()
    serializer_class = PrincipalesSerializer

class PostreViewSet(MenuItemViewSet):
    queryset = Postre.objects.all()
    serializer_class = PostreSerializer

class BebidaViewSet(MenuItemViewSet):
    queryset = Bebida.objects.all()
    serializer_class = BebidaSerializer

# ViewSet para gestionar el Precio
class PrecioViewSet(viewsets.ModelViewSet):
    queryset = Precio.objects.all()
    serializer_class = PrecioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Método para validación personalizada en la creación de un nuevo objeto
    def create(self, request, *args, **kwargs):
        max_items = 1  # Límite máximo de 1 precio
        current_count = Precio.objects.count()

        if current_count >= max_items:
            return Response(
                {
                    "error": f"Solo se puede crear {max_items} {Precio._meta.verbose_name_plural}."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().create(request, *args, **kwargs)

# APIView para obtener el número de ítems por tipo
# class GetNumItemsView(APIView):
#     def get(self, request, item_type):
#         # Mapa de los tipos de ítem a los modelos
#         model_map = {
#             "entrantes": Entrantes,
#             "principales": Principales,
#             "postre": Postre,
#             "bebida": Bebida,
#         }

#         model_class = model_map.get(item_type)

#         if not model_class:
#             return Response({"error": "Tipo de ítem inválido"}, status=status.HTTP_400_BAD_REQUEST)

#         num_items = model_class.objects.count()
#         return JsonResponse({"num_items": num_items})
