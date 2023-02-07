from rest_framework import serializers
from .models import User

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