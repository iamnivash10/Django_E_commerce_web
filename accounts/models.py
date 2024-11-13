from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email, password = None):
        if not email:
            raise ValueError("email must be needed")
        if not username:
            raise ValueError("username is needed")
        
        user = self.model(
               email = self.normalize_email(email),
               first_name = first_name,
               last_name = last_name,
               username = username)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
            username=username
        )
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=100,unique=True)
   
    #required

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin =  models.BooleanField(default=False)
    is_superuser =  models.BooleanField(default=False)
    
    objects = MyAccountManager()

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    class Meta:
        # Avoiding clashes by using different related names
        swappable = 'AUTH_USER_MODEL'
    
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'account'
        verbose_name_plural = 'accounts'

    def has_perms(self, perms, obj=None):
      if self.is_superuser:
        return True
    # Optionally, check if user has specific permissions
      return self.is_admin

    def has_module_perms(self, add_label):
      return self.is_staff  # Adjust according to your requirements


