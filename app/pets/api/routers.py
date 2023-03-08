from rest_framework import routers
from .views import PetViewSet

router = routers.SimpleRouter()
router.register(r"pets", PetViewSet)

urlpatterns = router.urls
