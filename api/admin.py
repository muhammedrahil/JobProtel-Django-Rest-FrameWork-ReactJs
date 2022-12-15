from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(WebsiteBasicDeatails)
admin.site.register(Countries)
admin.site.register(JobType)


