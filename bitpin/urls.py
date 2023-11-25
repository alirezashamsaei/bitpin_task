from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import BlogPostViewSet, RatingViewSet, UserViewSet,RateViewSet

router = DefaultRouter()
router.register(r'blogposts', BlogPostViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rate/', RateViewSet.as_view({'get': 'list'})),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]