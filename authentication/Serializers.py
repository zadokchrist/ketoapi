from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class RegistrationSerialiser(serializers.ModelSerializer):
    #Password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['Firstname','LastName','Username','Email','PhoneNumber']
    
    def validate(self, attrs):
        firstname = attrs.get('Firstname','')
        LastName = attrs.get('LastName','')
        PhoneNumber = attrs.get('PhoneNumber','')

        if not PhoneNumber.isnumeric():
            raise serializers.ValidationError('PhoneNumber should only be numbers')
        elif not firstname.isalnum():
            raise serializers.ValidationError('Firsname should be alpha numeric')
        elif not LastName.isalnum():
            raise serializers.ValidationError('Firsname should be alpha numeric')
        return attrs
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['FirstName','LastName','Username','Email','PhoneNumber']

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)
    tokens = serializers.CharField(read_only=True)
    Email = serializers.EmailField()
    Firstname = serializers.CharField(read_only=True)
    LastName = serializers.CharField(read_only=True)
    PhoneNumber = serializers.CharField(read_only=True)


    class Meta:
        model = User
        fields = ['Email','username','password','tokens','Firstname','LastName','PhoneNumber']

    def validate(self, attrs):
        username = attrs.get('Email','')
        password = attrs.get('password','')
        print('***************************')
        print(f'Username : {username} password : {password}')
        print('***************************')
        user = auth.authenticate(email=username,password=password)
        print('***************************')
        print(user)
        print('***************************')
        if not user:
            raise AuthenticationFailed('Invalid Username or Password')
        if not user.Is_active:
            raise AuthenticationFailed('User not Active')
        if not user.Is_Varified:
            raise AuthenticationFailed('Please verify your email address')

        return {
            'email': user.Email,
            'username': user.Username,
            'firstname': user.Firstname,
            'LastName': user.LastName,
            'PhoneNumber': user.PhoneNumber,
            'tokens': user.tokens
        }
