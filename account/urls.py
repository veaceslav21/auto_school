from django.urls import path
from .views import AccountRegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/', AccountRegisterView.as_view(), name='account_register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh', TokenRefreshView.as_view(), name='refresh_token'),
]