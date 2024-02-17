from django.contrib import admin
from .models import Spareparts

# Register your models here.

class SparePartsAdmin(admin.ModelAdmin):
    list_display = ('spare_part_name', )
    list_display_links = ('spare_part_name',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(Spareparts, SparePartsAdmin)
