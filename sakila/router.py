from rest_framework import routers
from sakila.views import ActorViewSet

router = router.router = routers.DefaultRouter()
router.register('actors', ActorViewSet, 'actors')