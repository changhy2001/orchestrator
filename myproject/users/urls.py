from django.urls import path
from . import views
from .api_views import register_api, login_api, logout_api

app_name = 'users'

urlpatterns = [
    path('api/register/', register_api, name='api_register'),
    path('api/login/', login_api, name='api_login'),
    path('api/logout/', logout_api, name='api_logout'),
]