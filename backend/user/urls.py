from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserViewSet, UserRoleUpdate

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')

urlpatterns = router.urls

urlpatterns += [
    path('login/', obtain_auth_token),
    path('user/<int:pk>/role/', UserRoleUpdate.as_view())
]
