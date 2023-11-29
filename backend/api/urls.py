from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    #  Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.
    TokenObtainPairView,
    #  Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.
    TokenRefreshView,
    # Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular use.
    TokenVerifyView,
)


urlpatterns = [
    
    path('auth/', obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', views.api_homeGet),
    path('post/', views.api_homePost)
]