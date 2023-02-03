from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,phone_number,first_name,last_name):
        self.db.create()
    def create_superuser(self,phone_number,first_name,last_name):
        pass



class User(AbstractBaseUser):
    phone_number=models.CharField(max_length=12)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    active=models.BooleanField(default=False)
    REQUIRED_FIELDS=[]
    USERNAME_FIELD='phone_number'
    objects=UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def is_active(self):
        return self.active    