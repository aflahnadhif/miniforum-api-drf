from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register('post', PostViewSet, basename='post')
router.register('comment', CommentViewSet, basename='comment')

urlpatterns = router.urls
