from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('login/', views.loginPage, name="loginPage"),
    path('search/', views.search, name="search"),
    path('register/', views.register, name="register"),
    path('logout/', views.logoutPage, name="logoutPage"),
]
