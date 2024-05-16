from django.urls import path, include, re_path
from .views import *


urlpatterns = [
    re_path(
        r'^o/(?P<provider>\S+)/$',
        CustomProviderAuthView.as_view(),
        name='provider-auth'
    ),
    path('register/', CustomUserRegisterView.as_view(), name='user-create'),
    path('activate/', CustomActivationView.as_view(), name='activate'),
    path('resend-otp/', SendOTPView.as_view(), name='send-otp'),
    path('logout/', LogoutView.as_view()),
    path('', include('djoser.urls')),
    path('', include('djoser.social.urls')),
    path('login/', CustomTokenObtainPairView.as_view()),
    path('jwt/refresh/', CustomTokenRefreshView.as_view()),
    path('jwt/verify/', CustomTokenVerifyView.as_view()),
]