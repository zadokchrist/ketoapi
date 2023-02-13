from django.shortcuts import render
from rest_framework import generics,status,views
from .Serializers import RegistrationSerialiser,LoginSerializer
from .models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .util import Util

# Create your views here.

class RegisterView(generics.CreateAPIView):
    serializer_class = RegistrationSerialiser
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(Email=user_data['Email'])

        token = RefreshToken.for_user(user).access_token
        domain = get_current_site(request).domain
        relative_url = reverse('verify-email')
        absurl = 'http://'+domain+relative_url+'?token='+str(token)
        email_body = 'Hi '+user.Firstname+' '+user.LastName+',\n Use the link below to verify your email.\n'+absurl
        data = {
            'body' : email_body,
            'domain' :absurl,
            'email' : user.Email,
            'email_subject' : 'VERIFY EMAIL'
        }

        Util.sendMail(data=data)
        return Response(user_data,status=status.HTTP_201_CREATED)
    
class ListUsers(views.APIView):
    def get(self,request,format=None):
        users = User.objects.all()
        serializer = RegistrationSerialiser(users, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
