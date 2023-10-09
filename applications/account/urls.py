from django.urls import path
from .views import RegisterAPIView, ActivateAPIView, ChangePasswordAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('activate/<uuid:activation_code>/', ActivateAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('change_password/', ChangePasswordAPIView.as_view()),

]