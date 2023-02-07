from django.urls import path
from .views import RegisterView,ListUsers

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('getusers/',ListUsers.as_view(),name='getusers')
]