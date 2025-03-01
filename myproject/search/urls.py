from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('', views.search_view, name="search"),
    path("user/<str:username>/", views.detail, name="detail"),
]