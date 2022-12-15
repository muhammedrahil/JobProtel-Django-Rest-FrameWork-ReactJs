from django.db import models
from django.contrib.auth.models import  AbstractBaseUser,PermissionsMixin
from .manager import UserManager

class UserType(models.Model):
    type = models.CharField(max_length=255, blank=True,null=True)
    is_active           = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_ip = models.GenericIPAddressField(blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True)
    modified_ip = models.GenericIPAddressField(blank=True, null=True)
    record_status = models.CharField(
        max_length=255, default='created', blank=True, null=True)

class User(AbstractBaseUser,PermissionsMixin):
    email               = models.EmailField(max_length=100,unique=True)
    phone_no            = models.CharField(max_length=12, null=True, blank=True,)
    first_name          = models.CharField(max_length=50, null=True, blank=True,)
    last_name           = models.CharField(max_length=50, null=True, blank=True,)
    user_type           = models.ForeignKey(UserType,on_delete=models.CASCADE,related_name="user_type",null=True, blank=True)
    is_admin            = models.BooleanField(default=False)
    is_staff            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_superadmin       = models.BooleanField(default=False)
    
    created_date = models.DateTimeField(auto_now_add=True)
    created_ip = models.GenericIPAddressField(blank=True, null=True)

    modified_date = models.DateTimeField(auto_now=True)
    modified_ip = models.GenericIPAddressField(blank=True, null=True)

    record_status = models.CharField(
        max_length=255, default='created', blank=True, null=True)
    
    objects =UserManager()
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS =['phone_no','first_name', 'last_name']
    
    def __str__(self) :
        return self.email
    
    def has_perm(self,prem,obj=None):
        return True
    
    def has_module_perms(self,app_lable):
        return True
    
    def fullname(self):
        return "{} {}".format(self.first_name,self.last_name)
    
    
    
    
    
