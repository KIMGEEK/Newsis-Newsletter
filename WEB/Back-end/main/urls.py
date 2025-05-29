from django.urls import include, path

from .views import PostViewSet, UserViewSet, DataViewSet

from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers



router = routers.SimpleRouter()
router.register('post', PostViewSet, basename='post')
router.register('user', UserViewSet, basename='user')
router.register('data', DataViewSet, basename='data')

urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
