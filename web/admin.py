from django.contrib import admin
from .models import Callback

# Register your models here.

class CallbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'service', 'created_at', 'updated_at')
    list_display_links = ('name', 'mobile')
    
admin.site.register(Callback, CallbackAdmin)
