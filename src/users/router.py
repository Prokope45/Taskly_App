from rest_framework import routers
from .viewsets import UserViewSets

app_name = "users"

router = routers.DefaultRouter()
router.register('users', UserViewSets)
