from django.contrib import admin
from django.urls import path
from .views import MyTokenObtainPairView, CreateUserView, currentUserView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('current_user/', currentUserView.as_view(), name='current_user')
]
