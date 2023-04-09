from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserViewSet

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')

urlpatterns = router.urls

urlpatterns += [
    path('api-token-auth/', obtain_auth_token),
]
