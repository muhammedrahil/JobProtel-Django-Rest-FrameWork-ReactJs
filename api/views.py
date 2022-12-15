from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from django.http import HttpResponse


class WebsiteBasicDeatailsApiView(ModelViewSet):
  serializer_class = WebsiteBasicDeatailsSerializer
  
  def get_queryset(self):
    result = WebsiteBasicDeatails.objects.all()
    return result
  
class CountriesApiView(ModelViewSet):
  serializer_class = CountriesSerializer
  
  def get_queryset(self):
    result = Countries.objects.all()
    return result


class JobTypeApiView(ModelViewSet):
  serializer_class = JobTypeSerializer
  
  def get_queryset(self):
    result = JobType.objects.all()
    return result 
  
  

 
from bs4 import BeautifulSoup
import requests




def temparay_use_fun(request): 
  state = ['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick', 'Newfoundland and Labrador', 'Northwest Territories', 'Nova Scotia', 'Nunavut', 'Ontario', 'Prince Edward Island', 'Quebec', 'Saskatchewan', 'Yukon Territory']

  for i in state:
    s = Countries()
    s.name = i
    # s.save()
  return HttpResponse('success',)