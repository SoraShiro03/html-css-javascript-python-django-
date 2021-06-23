from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from .models import Post



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



def profile(request):
   return render(request, "public_social.html")

