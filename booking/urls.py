from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="loginPage"),
    path('register/', views.register, name="register"),
    path('logout/', views.logoutPage, name="logoutPage"),
]
