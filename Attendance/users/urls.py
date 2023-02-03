from rest_framework.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from users.views import UserAPI

urlpatterns = [
    path('token/',TokenObtainPairView.as_view(),name='login'),
    path('token/refresh',TokenRefreshView.as_view(),name='refresh-login'),
    path('create-user',UserAPI.as_view(),name='create-user')
]