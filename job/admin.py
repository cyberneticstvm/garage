from django.contrib import admin
from .models import JobStatus, Job

# Register your models here.

class JobStatusAdmin(admin.ModelAdmin):
    list_display = ('status_name', )
    list_display_links = ('status_name',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class JobAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'brand_name', 'model_name', 'make_year', 'job_description', 'created_at', 'status')
    list_display_links = ('job_id',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(JobStatus, JobStatusAdmin)
admin.site.register(Job, JobAdmin)
