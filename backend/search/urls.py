from django.urls import path
from .views import SearchAPIView, SearchDetailAPIView

app_name = "search"

urlpatterns = [
    path('', SearchAPIView.as_view(), name='search_api'),
    path('<str:username>/', SearchDetailAPIView.as_view(), name='search_detail_api'),
]