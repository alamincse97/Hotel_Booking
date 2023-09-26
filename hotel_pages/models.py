from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class hotel(models.Model):
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
       
# class Review(models.Model):
#     Hotels = models.ForeignKey(hotel, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     review = models.TextField(max_length=500, blank=True)
#     rating = models.FloatField(max_length=5, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self) -> str:
#         return self.subject    

class Review(models.Model):
    hotel = models.ForeignKey(hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
 
    def __str__(self):
        return f"Review by {self.user.username} for {self.hotel.Name}"

    
    