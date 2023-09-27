from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hotel(models.Model):
    Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    Country = models.CharField(max_length=200)
    PhoneNumber = models.CharField(max_length=12)
    description = models.TextField()
    image = models.ImageField(upload_to='hotel/images/')
    url = models.URLField(blank=True)
    
    def __str__(self) -> str:
        return self.Name 

class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
 
    def __str__(self) -> str:
        return str('self.user')  

    
    