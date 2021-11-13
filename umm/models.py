from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Mechanics(models.Model):
    identity=models.CharField(max_length=100, default="korola")
    
    
    
    def __str__(self):
        return self.identity
        
        
        

        
        
class Post(models.Model):
    address = models.CharField(max_length=100)
    comment = models.TextField()
    phone = models.CharField(max_length=100)
    age = models.DateTimeField(default=timezone.now)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    car=models.CharField(max_length=100, null=True)
    license = models.CharField(max_length=100)
    appointment=models.CharField(max_length=100)
    mechanic=models.ForeignKey(Mechanics,on_delete=models.CASCADE)
    
    



    def __str__(self):
        return self.address
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    


    

    















