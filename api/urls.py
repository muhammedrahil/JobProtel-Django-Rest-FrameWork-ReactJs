from django.urls import path,include
from . import views as v
from rest_framework.routers import DefaultRouter
app_name = 'api'
router = DefaultRouter()
router.register('webdeatails', v.WebsiteBasicDeatailsApiView,basename="webdeatails")
router.register('countries', v.CountriesApiView,basename="countries")
router.register('jobtypes', v.JobTypeApiView,basename="jobtypes")
router.register('jobs', v.JobsAPiView,basename="jobs")
router.register('letest-jobs', v.LetestJobsAPiView,basename="letest-jobs")





urlpatterns = [
      path('',include(router.urls)),
      path('temparay-use-fun',v.temparay_use_fun),
      path('jobqualification/<int:pk>/',v.JobQualificationView.as_view()),
      path('fulljobdescription/<int:pk>/',v.FullJobDescriptionView.as_view()),
      path('job-description/<int:pk>/',v.JobDescriptionView.as_view()),


      
      
]