from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

# Create your models here.

class MyAccountsManager(BaseUserManager):

    # method to create user 
    def create_user(self , first_name , last_name , username , email  , password = None):
        if not email:
            raise ValueError("User Must Have Email-ID ...")

        if not username:
            raise ValueError("User Must have Username ...")

        user = self.model( email = self.normalize_email(email) , username = username , first_name = first_name , last_name = last_name)
        user.is_active = True
        user.set_password(password)
        user.save(using = self._db)
        print("password :", password)
        return user


    #method to create superuser 
    def create_superuser(self , first_name , last_name , email , username , password):

        user = self.create_user(email = self.normalize_email(email) , username = username ,password = password, first_name = first_name , last_name = last_name )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True

        # print('user.is_superadmin :',user.is_superadmin)
        # print('user.is_staff :',user.is_staff)
        
        user.save(using = self._db)
        return user
    



# Steps - 1
class AccountModel(AbstractBaseUser):
    first_name      = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100)
    username        = models.CharField(max_length=100 , unique = True)
    email           = models.EmailField(max_length = 100 , unique = True )
    phone_number    = models.CharField(max_length = 100)

    # Required Fields 
    date_joined     = models.DateTimeField(auto_now_add = True)
    last_login      = models.DateTimeField(auto_now_add = True)
    is_admin        = models.BooleanField(default = False)
    is_staff        = models.BooleanField(default = False)
    is_active       = models.BooleanField(default = False)

    is_superadmin   = models.BooleanField(default = False)

    #this Field is used for login
    USERNAME_FIELD = 'email'  

    # this field is required for register new user
    REQUIRED_FIELDS = ['username' , 'first_name' , 'last_name']

    objects = MyAccountsManager()

    def __str__(self):
        return self.email

    # set for permissions 
    def has_perm(self , perms , obj = None):
        return self.is_admin

    def has_module_perms(self , add_label):
        return True