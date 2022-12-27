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
    
class CitySerializer(ModelSerializer):
  class Meta:
    model = City
    fields = '__all__'
    depth = 3
    
class JobTypeSerializer(ModelSerializer):
  class Meta:
    model = JobType
    fields = '__all__'


class JobsSerializer(ModelSerializer):
  class Meta:
    model = Jobs
    fields = '__all__'
    depth = 1
    
class JobQualificationSerializer(ModelSerializer):
    class Meta:
      model = Qualification
      fields = '__all__'
      depth = 1
      
      
class FullJobDescriptionSerializer(ModelSerializer):
    class Meta:
      model = FullJobDescription
      fields = '__all__'
      depth = 1
      
      
class JobDescriptionSerializer(ModelSerializer):
    class Meta:
      model = job_description
      fields = '__all__'
      depth = 1