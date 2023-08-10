from django.urls import path
from rest_framework import routers

from apps.users.views import UserViewSet

router = routers.DefaultRouter()

router.register('', UserViewSet)

urlpatterns = router.urls
