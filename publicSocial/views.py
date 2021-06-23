from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .forms import RegisterForm, UserForm
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users


def home(request):
   posts = Post.objects.all()
   posts = {'posts': posts}
   return render(request,"public_social/base.html", posts) 


def register(request):
   form = RegisterForm()
   if request.method == 'POST':
      form = RegisterForm(request.POST)
      if form.is_valid():
         form.save()
         user = form.cleaned_data.get('username')
         username = form.cleaned_data.get('username')
         return redirect('login')
   
   else:
      form = RegisterForm()
   return render(request, 'public_social/register.html', {'form':form})


@login_required
#@allowed_users(allowed_roles=['user'])
def profile(request):
   user = request.user.profile
   form = UserForm( instance=user)
   if request.method == 'POST':
      form = UserForm(request.POST, request.FILES, instance=user)
      if form.is_valid():
         form.save()

   context ={'form': form}

   return render(request, "public_social/profile.html", context)

