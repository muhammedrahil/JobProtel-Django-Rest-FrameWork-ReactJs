from django.db import models

# Create your models here.

class WebsiteBasicDeatails(models.Model):
  logo = models.ImageField(upload_to="logos",blank=True,null=True)
  name = models.CharField(max_length=255,null=True,blank=True)
  
  def __str__(self) -> str:
    return self.name


class Countries(models.Model):
  name = models.CharField(max_length=255,null=True, blank=True)
  
  def __str__(self) -> str:
    return self.name
  
  
class JobType(models.Model):
  name = models.CharField(max_length=255,null=True, blank=True)
  
  def __str__(self) -> str:
    return self.name