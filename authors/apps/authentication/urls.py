from django.conf.urls import url
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView
)


urlpatterns = [
    url(r'^user/?$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^users/?$', RegistrationAPIView.as_view(), name='authentication'),
    url(r'^users/login/?$', LoginAPIView.as_view(), name='login'),
    path('token', TokenObtainPairView.as_view()), 
    path('token/refresh', TokenRefreshView.as_view()),
]
