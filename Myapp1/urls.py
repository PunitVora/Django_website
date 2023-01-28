from django.urls import path #to use path()
from . import views #to use views

urlpatterns = [

    path('', views.Index, name ='Index'), 
    path('Register', views.Register, name = 'Register' ),
    path('Login', views.Login, name = 'Login'),
    path('Logout', views.Logout, name = 'Logout')
 
]