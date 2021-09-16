from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User





class Post(models.Model):
    title = models.CharField(max_length=100)
    no = models.TextField()
    age = models.DateTimeField(default=timezone.now)
    name = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return self.title


class Phone(models.Model):

    Model = models.CharField(max_length=100)
    Brand=models.CharField(max_length=100)
    Description = models.TextField()
    Posted = models.DateTimeField(default=timezone.now)
    image_url=models.CharField(max_length=2083)
    Price=models.FloatField()
    Size=models.FloatField()

    def __str__(self):
        return self.Model







class Review(models.Model):
    pt = models.ForeignKey(User, on_delete=models.CASCADE)
    on=models.ForeignKey(Phone,on_delete=models.CASCADE)
    text=models.TextField()

    def __str__(self):
        return str(self.on)

















