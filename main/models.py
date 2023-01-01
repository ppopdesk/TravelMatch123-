from django.db import models
import datetime 
# Create your models here.
class UserInfo(models.Model):
    email = models.EmailField()
    phone_number = models.IntegerField()
    username = models.CharField(max_length=150)
    destination = models.CharField(max_length=20)
    arrival = models.DateTimeField(default=datetime.datetime.now())
    preferred_transport = models.CharField(max_length=20)
    submitted = models.BooleanField(default=False)

    def __str__(self):
        return self.username + str(self.submitted)