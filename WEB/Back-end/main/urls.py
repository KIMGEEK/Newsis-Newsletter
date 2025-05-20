from django.urls import include, path

from .views import PostViewSet, UserCreateViewSet

from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers



router = routers.DefaultRouter()
router.register('post', PostViewSet, basename='post')
router.register('subscribe', UserCreateViewSet, basename='subscribe')

urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
