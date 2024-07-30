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




# #handles username validation
# #meaning it will check in database if username exists or not so that the user does not use it
# #it will send back data in form of json

# class UsernameValidationView(View):
#     #this is used because a user will be sending a GET request to confirm availability of username

#     def post(self,request):#it is a POST request because user is sending the data(username)

#         data = json.loads(request.body)#the variable data will contain the username data
#         #loads will act as a python dictionary from which the username can be accessed 
#         username = data['username']
#         #allow system to pick the username from the data posted

#         if not str(username).isalnum():
#             #this condidtion will check the data that is not alphanumeric
#             return JsonResponse({'username_error':'username should only contain letters and numbers'}, status=400)
#             #the 400 is used to show that the request is bad because it showed 200 which meant OK
#             #this message is like a HttpResponse displayed to the user

#         #this will check is username has been already used/already exists in database
#         if User.objects.filter(username=username).exists():
#             #this will check if username exixts
#             #if true it will return message below

#             return JsonResponse({'username_error':'sorry username in use, choose another one'}, status=409)
#             #the 400 is used to show that the request is bad because it showed 200 which meant OK
#             #this message is like a HttpResponse displayed to the user

#         return JsonResponse({'username_valid': True})   
# #an API call will be made using postman         




        
