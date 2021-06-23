from .models import Post, Profile
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields

class RegisterForm(UserCreationForm):
  

   class Meta:
      model = User
      fields = ['username', 'email', 'password1', 'password2']


class UserForm(ModelForm):

   class Meta:
      model = Profile
      fields = '__all__'
      exclude = ['user']