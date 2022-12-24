from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(WebsiteBasicDeatails)
admin.site.register(Countries)
admin.site.register(JobType)
admin.site.register(States)
admin.site.register(City)
admin.site.register(Company)
admin.site.register(Jobs)
admin.site.register(JobTypeShift)
admin.site.register(JobTypes)
admin.site.register(Qualification)
admin.site.register(FullJobDescription)
admin.site.register(job_description)






