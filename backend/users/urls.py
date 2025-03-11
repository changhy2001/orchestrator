from django.urls import path
from . import views
from .views import RegisterAPIView, LoginAPIView, LogoutAPIView, AuthStatusAPIView

app_name = 'users'

urlpatterns = [
    path('auth-status/', AuthStatusAPIView.as_view(), name='api_auth_status'),
    path('register/', RegisterAPIView.as_view(), name='api_register'),
    path('login/', LoginAPIView.as_view(), name='api_login'),
    path('logout/', LogoutAPIView.as_view(), name='api_logout'),
]