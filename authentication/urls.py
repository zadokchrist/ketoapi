from django.urls import path
from .views import RegisterView,ListUsers,LoginView

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('getusers/',ListUsers.as_view(),name='getusers'),
    path('Login/',LoginView.as_view(),name='Login'),
    path('verifyuser/',ListUsers.as_view(),name='verify-email'),
]