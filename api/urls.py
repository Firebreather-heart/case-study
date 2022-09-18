from django.urls import path 
from .views import PostViewset

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
#router.register('users',UserViewset, basename='users')
router.register('',PostViewset, basename='posts')
urlpatterns = router.urls