from django.db import models
from accounts.models import User
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
  
class States(models.Model):
  country = models.ForeignKey(Countries,on_delete=models.CASCADE,related_name="country")
  name = models.CharField(max_length=255,null=True, blank=True)
  
  def __str__(self) -> str:
    return self.name
  
class City(models.Model):
  state = models.ForeignKey(States,on_delete=models.CASCADE,related_name="state")
  name = models.CharField(max_length=255,null=True, blank=True)
  
  def __str__(self) -> str:
    return self.name
  
  # diffrent Jobs model
class JobType(models.Model):
  name = models.CharField(max_length=255,null=True, blank=True)
  
  def __str__(self) -> str:
    return self.name



class Company(models.Model):
  name = models.CharField(max_length=255,null=True,blank=True)
  website_link = models.URLField(blank=True,null=True)
  
  is_active       =   models.BooleanField(default=True)
  created_date    =   models.DateTimeField(auto_now_add=True)
  created_id      =   models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,related_name='company_created_id')
  created_ip      =   models.GenericIPAddressField(blank=True,null=True)
  modified_date   =   models.DateTimeField(auto_now=True)
  modified_id     =   models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,related_name='company_modified_id')
  modified_ip     =   models.GenericIPAddressField(blank=True,null=True)
  record_status   =   models.CharField(max_length=255,default='created') 
  
  def __str__(self) -> str:
    return self.name


# jobtypes  
class JobTypes(models.Model):
  type1 = models.CharField(max_length=255,null=True, blank=True)
  type2 = models.CharField(max_length=255,null=True, blank=True)
  type3 = models.CharField(max_length=255,null=True, blank=True)
  type4 = models.CharField(max_length=255,null=True, blank=True)
  type5 = models.CharField(max_length=255,null=True, blank=True)
  type6 = models.CharField(max_length=255,null=True, blank=True)
  
  
  is_active       =   models.BooleanField(default=True)
  created_date    =   models.DateTimeField(auto_now_add=True)
  created_id      =   models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,related_name='jobtypes_created_id')
  created_ip      =   models.GenericIPAddressField(blank=True,null=True)
  modified_date   =   models.DateTimeField(auto_now=True)
  modified_id     =   models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,related_name='jobtypes_modified_id')
  modified_ip     =   models.GenericIPAddressField(blank=True,null=True)
  record_status   =   models.CharField(max_length=255,default='created')  
  
  def __str__(self) -> str:
    return self.type1
  
  


# shifting  
class JobTypeShift(models.Model):
  shift1 = models.CharField(max_length=255,null=True, blank=True)
  shift2 = models.CharField(max_length=255,null=True, blank=True)
  shift3 = models.CharField(max_length=255,null=True, blank=True)
  shift4 = models.CharField(max_length=255,null=True, blank=True)
  shift5 = models.CharField(max_length=255,null=True, blank=True)
  shift6 = models.CharField(max_length=255,null=True, blank=True)
  
  is_active       =   models.BooleanField(default=True)
  created_date    =   models.DateTimeField(auto_now_add=True)
  created_id      =   models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,related_name='jobtypeshift_created_id')
  created_ip      =   models.GenericIPAddressField(blank=True,null=True)
  modified_date   =   models.DateTimeField(auto_now=True)
  modified_id     =   models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,related_name='jobtypeshift_modified_id')
  modified_ip     =   models.GenericIPAddressField(blank=True,null=True)
  record_status   =   models.CharField(max_length=255,default='created')  
  
  def __str__(self) -> str:
    return self.shift1

class Jobs(models.Model):
  job_name = models.ForeignKey(JobType,on_delete=models.CASCADE,related_name="job_name",null=True, blank=True)
  company_name = models.ForeignKey(Company,on_delete=models.CASCADE,related_name="company_name",null=True, blank=True)
  company_city = models.ForeignKey(City,on_delete=models.DO_NOTHING,related_name="company_city",null=True, blank=True)
  company_state = models.ForeignKey(States,on_delete=models.DO_NOTHING,related_name="company_state",null=True, blank=True)
  company_contry = models.ForeignKey(Countries,on_delete=models.DO_NOTHING,related_name="company_contry",null=True, blank=True)
  company_jobtypes = models.ForeignKey(JobTypes,on_delete=models.DO_NOTHING,related_name="company_jobtypes",null=True, blank=True)
  company_jobshifts = models.ForeignKey(JobTypeShift,on_delete=models.DO_NOTHING,related_name="company_jobshifts",null=True, blank=True)
  
  start_month_salary = models.CharField(max_length=255,null=True, blank=True)
  end_month_salary = models.CharField(max_length=255,null=True, blank=True)
  job_lpa = models.CharField(max_length=255,null=True, blank=True)
  company_phone_number = models.CharField(max_length=255,null=True, blank=True)
  
  is_active       =   models.BooleanField(default=True)
  created_date    =   models.DateTimeField(auto_now_add=True)
  created_id      =   models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,related_name='job_created_id')
  created_ip      =   models.GenericIPAddressField(blank=True,null=True)
  modified_date   =   models.DateTimeField(auto_now=True)
  modified_id     =   models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,related_name='job_modified_id')
  modified_ip     =   models.GenericIPAddressField(blank=True,null=True)
  record_status   =   models.CharField(max_length=255,default='created')   

  class Meta:
      ordering = ('-created_date',)

  def __str__(self) -> str:
    return f"{self.job_name.name}"
 

  
class Qualification(models.Model):
  job = models.ForeignKey(Jobs,on_delete=models.CASCADE,related_name="job_qualifications")
  qualification = models.CharField(max_length=255,null=True, blank=True)
  totel_year = models.CharField(max_length=255,null=True, blank=True)
  
  is_active       =   models.BooleanField(default=True)
  created_date    =   models.DateTimeField(auto_now_add=True)
  created_id      =   models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,related_name='qualification_created_id')
  created_ip      =   models.GenericIPAddressField(blank=True,null=True)
  modified_date   =   models.DateTimeField(auto_now=True)
  modified_id     =   models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,related_name='qualification_modified_id')
  modified_ip     =   models.GenericIPAddressField(blank=True,null=True)
  record_status   =   models.CharField(max_length=255,default='created')  
  
  def __str__(self) -> str:
    return self.qualification
    
  
class FullJobDescription(models.Model):
  job = models.ForeignKey(Jobs,on_delete=models.CASCADE,related_name="job_full_job_description")
  framework = models.CharField(max_length=255,null=True, blank=True)
  start_experince = models.CharField(max_length=255,null=True, blank=True)
  end_experince = models.CharField(max_length=255,null=True, blank=True)
  job_type = models.CharField(max_length=255,null=True, blank=True)

  is_active       =   models.BooleanField(default=True)
  created_date    =   models.DateTimeField(auto_now_add=True)
  created_id      =   models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,related_name='job_full_job_description_created_id')
  created_ip      =   models.GenericIPAddressField(blank=True,null=True)
  modified_date   =   models.DateTimeField(auto_now=True)
  modified_id     =   models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,related_name='job_full_job_description_modified_id')
  modified_ip     =   models.GenericIPAddressField(blank=True,null=True)
  record_status   =   models.CharField(max_length=255,default='created')  
  


class job_description(models.Model):
  job = models.ForeignKey(Jobs,on_delete=models.CASCADE,related_name="job_description")
  job_description = models.CharField(max_length=500,null=True, blank=True)
  
  is_active       =   models.BooleanField(default=True)
  created_date    =   models.DateTimeField(auto_now_add=True)
  created_id      =   models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,related_name='job_description_created_id')
  created_ip      =   models.GenericIPAddressField(blank=True,null=True)
  modified_date   =   models.DateTimeField(auto_now=True)
  modified_id     =   models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,related_name='job_description_modified_id')
  modified_ip     =   models.GenericIPAddressField(blank=True,null=True)
  record_status   =   models.CharField(max_length=255,default='created')  

  def __str__(self) -> str:
    return self.job_description[:40]