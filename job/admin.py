from django.contrib import admin
from .models import JobStatus, Job, JobSparePart, JobService

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
    
class JobSparePartAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'spare_part_id', 'qty', 'cost_per_unit', 'total', 'staff', 'created_at')
    list_display_links = ('spare_part_id',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class JobServiceAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'description', 'fee', 'created_at')
    list_display_links = ('description',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(JobStatus, JobStatusAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobSparePart, JobSparePartAdmin)
admin.site.register(JobService, JobServiceAdmin)
