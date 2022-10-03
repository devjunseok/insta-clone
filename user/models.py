from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings

# Create your models here.
class UserModel(AbstractBaseUser):
    class Meta:
        db_table = "my_user"
        
    # follow = models.ManyToManyField(settings.AUTH_UESR_MODEL,related_name='followee')
    
