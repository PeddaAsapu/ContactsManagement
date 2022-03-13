from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
# Create your models here.

class ContactsApp(models.Model) :
    #user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    user = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200,null=True)
    phone_number = models.IntegerField(default=None, blank=True, null=True)
    email = models.CharField(max_length=200,null=True )

    #def __str__(self) :
    #    return self.name

