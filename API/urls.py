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
