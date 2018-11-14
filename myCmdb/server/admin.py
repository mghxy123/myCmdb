from django.contrib import admin
from server.models import *
# Register your models here.

class apiInfoAdmin(admin.ModelAdmin):
    list_display = ['doc']

admin.site.register(api_info,apiInfoAdmin)