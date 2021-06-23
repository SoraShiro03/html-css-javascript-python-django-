from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
   path('', views.home, name='home'), # this name was assign variable.
   path('register/', views.register, name='register'),
   path('login/', auth_view.LoginView.as_view(template_name="public_social/login.html"), name='login'),
   path('logout/', auth_view.LogoutView.as_view(template_name="public_social/logout.html"), name='logout'),
   path('profile/', views.profile, name='profile')
]
