from django.shortcuts import render
from rest_framework import generics,status,views
from .Serializers import RegistrationSerialiser,UsersSerializer
from .models import User
from rest_framework.response import Response

# Create your views here.

class RegisterView(generics.CreateAPIView):
    serializer_class = RegistrationSerialiser
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(user_data,status=status.HTTP_201_CREATED)
    
class ListUsers(views.APIView):
    def get(self,request,format=None):
        users = User.objects.all()
        serializer = RegistrationSerialiser(users, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)