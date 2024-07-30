
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . models import Bank
from . models import Branch

# from django.contrib.auth.forms import AuthenticationForm
# from django.forms.widgets import PasswordInput, TextInput


# #create a form that will allow a  to be added
# class CreateRecordForm(forms.ModelForm):#making custom model form
#     class Meta:
#         model = Bank
#         fields = ['first_name', 'last_name', 'email', 'phone']


# #update a form that will allow a record to be added
# class UpdateRecordForm(forms.ModelForm):#making custom model form
#     class Meta:
#         model = Branch
#         fields = ['first_name', 'last_name', 'email', 'phone']




# # register or create user

# class CreateUserForm(UserCreationForm):#this is related to the register form
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']


# #login a user
# class LoginForm(AuthenticationForm):
#     username = forms.CharField(widget=TextInput())
#     password = forms.CharField(widget=PasswordInput())