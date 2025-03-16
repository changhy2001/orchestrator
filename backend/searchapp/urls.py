from django.urls import path
from .views import SearchUserMetaAPIView, SearchUserMetaDetailAPIView

app_name = "searchapp"

urlpatterns = [
    path('usermeta/', SearchUserMetaAPIView.as_view(), name='usermeta'),
    path('usermeta/<int:pk>/', SearchUserMetaDetailAPIView.as_view(), name='usermeta_detail'),
]