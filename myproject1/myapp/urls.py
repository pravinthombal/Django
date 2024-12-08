from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .views import ProfileViewSet



router = DefaultRouter()
# router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]



# from django.urls import path
# from .views import ProfileViewSet  # Import your ProfileViewSet

# urlpatterns = [
#     path('profiles/', ProfileViewSet.as_view(), name='profile-create')
# ]
