from rest_framework.serializers import ModelSerializer
from .models import *



class WebsiteBasicDeatailsSerializer(ModelSerializer):
  class Meta:
    model = WebsiteBasicDeatails
    fields = '__all__'
    
class CountriesSerializer(ModelSerializer):
  class Meta:
    model = Countries
    fields = '__all__'
    
    
class JobTypeSerializer(ModelSerializer):
  class Meta:
    model = JobType
    fields = '__all__'
