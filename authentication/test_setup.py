from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetup(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.user_data ={
            "Firstname": "Daniel",
            "LastName": "Ngobi",
            "Username": "daniel",
            "Email": "ngobidaniel04@gmail.com",
            "PhoneNumber": "0779226226"
            }
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()