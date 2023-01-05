from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.views import APIView
from .models import *
from django.http import HttpResponse
from .pagination import StandardResultsSetPagination
from rest_framework.response import Response
from rest_framework import status

from bs4 import BeautifulSoup
import json
import requests

class WebsiteBasicDeatailsApiView(ModelViewSet):
    serializer_class = WebsiteBasicDeatailsSerializer

    def get_queryset(self):
        result = WebsiteBasicDeatails.objects.all()
        user = self.request.user
        print(user)
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



class JobsAPiView(ModelViewSet):
    serializer_class = JobsSerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        return Jobs.objects.all().order_by('-created_date')

class LetestJobsAPiView(ModelViewSet):
    serializer_class = JobsSerializer
    def get_queryset(self):
        return Jobs.objects.values("id").order_by('-created_date')[:1]


class JobQualificationView(APIView):
    serializer_class = JobQualificationSerializer
    
    def get(self, request,pk=None):
        result = Qualification.objects.filter(job=pk)
        serializer = self.serializer_class(result,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class FullJobDescriptionView(APIView):
    serializer_class = FullJobDescriptionSerializer
    
    def get(self, request,pk=None):
        result = FullJobDescription.objects.filter(job=pk)
        serializer = self.serializer_class(result,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
class JobDescriptionView(APIView):
    serializer_class = JobDescriptionSerializer
    
    def get(self, request,pk=None):
        result = job_description.objects.filter(job=pk)
        serializer = self.serializer_class(result,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


def temparay_use_fun(request):
    url = "https://www.universal-tutorial.com/api/getaccesstoken"
    headers = {
        "Accept": "application/json",
        "api-token": "w_R2Ke09lJwTy1MIfPPx6KJ_aFbLYUtyA5V_jL6rml8ctnkYqAVW-kofZ26QTEa-1m4",
        "user-email": "muhammedrahilmadathingal@gmail.com"
    }
    response = requests.request("GET", url, headers=headers)
    token = response.json()
    url = "https://www.universal-tutorial.com/api/countries/"
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer "+token["auth_token"]
    }
    response = requests.request("GET", url, headers=headers)
    # for i in response.json():
    #   print(i["country_name"])
    #   contry_instence = Countries()
    #   contry_instence.country_name = i["country_name"]
    #   contry_instence.save()
    #   url_state = f"https://www.universal-tutorial.com/api/states/{i['country_name']}"
    #   response_state = requests.request("GET", url_state, headers=headers)
    #   try:
    #     for i in response_state.json():
    #       state_instances = States()
    #       state_instances.country = contry_instence
    #       state_instances.state_name = i["state_name"]
    #       state_instances.save()
    #       url_city = f"https://www.universal-tutorial.com/api/cities/{i['state_name']}"
    #       response_city = requests.request("GET", url_city, headers=headers)
    #       try : 
    #         for i in response_city.json():
    #           city_instances = City()
    #           city_instances.state = state_instances
    #           city_instances.city_name = i["city_name"]
    #           city_instances.save()
    #       except:
    #         pass
    #   except:
    #     pass
    return HttpResponse("success")
