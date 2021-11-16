from rest_framework import routers
from . import viewset

router = routers.DefaultRouter()

router.register("carts/", viewset.CartViewset, basename="carts")
urlpatterns = router.urls
