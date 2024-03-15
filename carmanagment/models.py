from django.db import models
from django.contrib.auth.models import User


class Car (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    manufacturer = models.CharField(max_length=100)
    year = models.IntegerField()
    image = models.ImageField('car_image/')  # картинка (впереди /)
    file = models.FileField('car_file/')  # файл


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=100)
    birthday = models.DateField()
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    avatar = models.ImageField('/avatar/')
