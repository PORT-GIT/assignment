from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views import View
#this view class has all the logic to handle requests and responses
import json

# Create your views here.

#simply renders registration page
class RegistrationView(View):

    def get(self,request):
        #this wiil handle GET requests
        #this means that when someone is requesting to view page then the command below will render the html page
        
        return render(request, 'accounts/register.html')
        #the html is found on the authentications folder in templates and not the django app 

#simply renders login page
class LoginView(View):

    def get(self,request):
        #this wiil handle GET requests
        #this means that when someone is requesting to view page then the command below will render the html page
        
        return render(request, 'accounts/login.html')
        #the html is found on the authentications folder in templates and not the django app 

# #simply renders registration page
# class LogoutView(View):

#     def get(self,request):
        #this wiil handle GET requests
        #this means that when someone is requesting to view page then the command below will render the html page
        
        # return render(request, 'accounts/register.html')
        # #the html is found on the authentications folder in templates and not the django app 



        
