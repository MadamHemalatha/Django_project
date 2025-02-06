from django.urls import path
from app2 import views

urlpatterns=[
    path('',views.homeView,name="homepage"),
    path('login',views.loginView,name="loginpage"),
    path('logout',views.logoutView,name="logoutpage"),
    path('profile',views.profileView,name="profilepage"),
    path('register',views.registerView,name="registerpage"),
    path('create',views.createView,name="createpage"),
    path('single',views.singleView,name="singlepage"),
    
    
]