from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import UserViewSet, BlogViewSet, BlogRatingViewSet, CommentViewSet, LikeViewSet, RegisterViewSet
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

router = DefaultRouter()

router.register("register", RegisterViewSet)
# router.register('users', UserViewSet)
router.register('blogs', BlogViewSet)
router.register('ratings', BlogRatingViewSet)
router.register('comments', CommentViewSet)
router.register('likes', LikeViewSet)

urlpatterns = [
    
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),

]
