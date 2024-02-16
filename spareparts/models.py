from django.db import models

# Create your models here.

class Spareparts(models.Model):
    spare_part_name = models.CharField(max_length=150, blank=True, null=True)
    cost_per_unit   = models.DecimalField(max_digits=7, decimal_places=2)
    
    REQUIRED_FIELDS = ['spare_part_name', 'cost_per_unit']
    
    def __str__(self):
        return str(self.spare_part_name) + ": ₹" + str(self.cost_per_unit)
