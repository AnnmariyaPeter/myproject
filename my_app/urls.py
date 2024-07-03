


from django.urls import path,include
from . import views

urlpatterns = [

    path('register',views.Register_user,name='register'),
    path('login/',views.loginUser,name='login'),
    path('logOut/',views.logOut,name='logOut'),
    path('home/',views.HomePage,name='home')
]