from rest_framework import routers
from .api import ProfileViewSet, UserViewSet

from django.urls import path
from .views import SignUpUser, SignInUser, SignOutUser, user_ads, UserProfile, EditProfile


urlpatterns = [
    path('signin/', SignInUser, name = 'login'),
    path('signup/', SignUpUser, name = 'register'),
    path('signout/', SignOutUser, name = 'logout'),
    
    path('profile/<int:user_id>/', UserProfile, name = 'profile'),
    path('edit_profile/<int:user_id>/', EditProfile, name = 'edit_profile'),
       
    path('myads/', user_ads, name = 'myads'),
    
]

router = routers.DefaultRouter()

router.register(r'api/profiles', ProfileViewSet, basename='profiles')

router.register(r'api/users', UserViewSet, basename='users')
urlpatterns += router.urls