from django.db import models

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
    