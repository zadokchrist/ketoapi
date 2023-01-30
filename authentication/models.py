from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self, Firstname,LastName,Username,Email,PhoneNumber,Password=None):
        if Firstname is None:
            raise TypeError('First Name is Required')
        elif LastName is None:
            raise TypeError('Last Name is Required')
        elif Username is None:
            raise TypeError('Username is Required')
        elif Email is None:
            raise TypeError('Username is Required')

        user = self.model(Firstname=Firstname,LastName=LastName,Username=Username,Email=self.normalize_email(Email),PhoneNumber=PhoneNumber)
        user.set_password(Password)
        user.save()
    
    def create_super_user(self, Firstname,LastName,Username,Email,PhoneNumber,Password=None):
        if Firstname is None:
            raise TypeError('First Name is Required')
        elif LastName is None:
            raise TypeError('Last Name is Required')
        elif Username is None:
            raise TypeError('Username is Required')
        elif Email is None:
            raise TypeError('Email is Required')
        
        user = self.create_user(Firstname,LastName,Username,Email,PhoneNumber)
        user.Is_Admin = True
        user.save()
        return user
    
class User(AbstractBaseUser,PermissionsMixin):
    Firstname = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Username = models.CharField(max_length=100,unique=True,db_index=True)
    Email = models.CharField(max_length=100,unique=True,db_index=True)
    PhoneNumber = models.CharField(max_length=13,unique=True,db_index=True)
    Is_Varified = models.BooleanField(default=False)
    Is_active = models.BooleanField(default=True)
    Created_At = models.DateTimeField(auto_now=True)
    Updated_At = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'Username'
    REQUIRED_FIELDS = ['Firstname','LastName','Email']

    objects = UserManager()

    def __str__(self) -> str:
        return self.Email

    def tokens(self):
        pass
