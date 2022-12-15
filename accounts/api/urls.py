from django.urls import path,include
from . import views as v
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from rest_framework.routers import DefaultRouter

app_name = 'accounts'
router = DefaultRouter()
router.register('user-type', v.UserTypeAPIView,basename="user-type")

urlpatterns = [
    path('token/', v.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
  
    path('registration/',v.UserRegstration.as_view(),name='registration'),
    path('users/',v.RetriveUsers.as_view(),name='users'),
    # path('user-type/',v.UserTypeAPIView.as_view({'get': 'list'}),name='user-type'),
    path('',include(router.urls)),
        
    
]