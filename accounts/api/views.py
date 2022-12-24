from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer, AccoutsSerializer, UserTypeSerializer
from accounts.models import UserType
User = get_user_model()


# get a user ip 
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# genarate token and add serializer_class and add user email

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserRegstration(APIView):
    def post(self, request):
        serilizer = AccoutsSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.validated_data['created_ip'] = get_client_ip(request)
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors, status=status.HTTP_404_NOT_FOUND)


class RetriveUsers(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serilizer = AccoutsSerializer(users, many=True)
        return Response(serilizer.data, status=status.HTTP_200_OK)


class UserTypeAPIView(ModelViewSet):
    serializer_class = UserTypeSerializer
    
    def get_queryset(self):
        result = UserType.objects.filter(is_active=True)
        return result

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['created_ip'] = get_client_ip(request)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        instence = get_object_or_404(UserType, pk=pk, is_active=True)
        serializer = self.get_serializer(instence, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['modified_ip'] = get_client_ip(request)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        instence = get_object_or_404(UserType, pk=pk, is_active=True)
        serializer = self.get_serializer(instence)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        instence = get_object_or_404(UserType, pk=pk, is_active=True)
        serializer = self.get_serializer(instence, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['is_active'] = False
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
            
            
    
    
    


