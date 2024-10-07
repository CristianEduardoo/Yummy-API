# Usamos routers en lugar de path, ya que nos permiten hacer varias operaciones CRUD
from rest_framework import routers
from .views import EntrantesViewSet, PrincipalesViewSet, PostreViewSet, BebidaViewSet, PrecioViewSet

app_name = "restaurant_api"

router = routers.DefaultRouter()  # Es clave porque lo gestiona Django (get, post, delete, etc..)
router.register("entrantes", EntrantesViewSet, "entrantes_api")
router.register("principales", PrincipalesViewSet, "principales_api")
router.register("postre", PostreViewSet, "postre_api")
router.register("bebida", BebidaViewSet, "bebida_api")
router.register("precio", PrecioViewSet, "precio_api")

urlpatterns = router.urls



# Código a mejorar!! 

""" 
from django.urls import path
from rest_framework import routers
from .views import EntrantesViewSet, PrincipalesViewSet, PostreViewSet, BebidaViewSet, PrecioViewSet, GetNumItemsView

app_name = "restaurant_api"

# Usamos routers para las operaciones CRUD automáticas de los viewsets
router = routers.DefaultRouter()  
router.register("entrantes", EntrantesViewSet, "entrantes_api")
router.register("principales", PrincipalesViewSet, "principales_api")
router.register("postre", PostreViewSet, "postre_api")
router.register("bebida", BebidaViewSet, "bebida_api")
router.register("precio", PrecioViewSet, "precio_api")

# Añadimos la ruta para la vista que obtiene el número de ítems
urlpatterns = router.urls + [
    path("num-items/<str:item_type>/", GetNumItemsView.as_view(), name="get_num_items"),
]
"""
