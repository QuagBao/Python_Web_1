from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.forms import UserCreationForm

class CustomUser(AbstractUser):
    user_id = models.AutoField(primary_key=True, null=False)
    date_birth = models.DateField(null=True, blank=False)
    phone_number = models.CharField(max_length=11, null=True, blank=False)
    
class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    cast = models.CharField(max_length=255)
    duration = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

class Theater(models.Model):
    theater_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

class Screening(models.Model):
    screening_id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
# # Đổi form register django
# class CreateUserForm (UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password1', 'password2']
