from django.urls import path, include
from .views import ListingViewSet, CommentViewSet, BidViewSet, CategoryViewSet
from users.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('listings', ListingViewSet)
router.register('categories', CategoryViewSet)
router.register('comments', CommentViewSet)
router.register('bids', BidViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
