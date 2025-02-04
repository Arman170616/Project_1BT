from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import HomePageContentListCreateView, HomePageContentRetrieveUpdateDestroyView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/home/', HomePageContentListCreateView.as_view(), name='home-page-list-create'),
    path('api/home/<int:pk>/', HomePageContentRetrieveUpdateDestroyView.as_view(), name='home-page-retrieve-update-destroy'),
]