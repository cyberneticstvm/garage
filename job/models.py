from django.db import models
from account.models import Account
from spareparts.models import Spareparts
# Create your models here.

class JobStatus(models.Model):
    status_name = models.CharField(max_length=25, unique=True)
    
    def __str__(self):
        return self.status_name

class Job(models.Model):
    job_id = models.CharField(max_length=10, blank=True)
    brand_name = models.CharField(max_length=100, blank=True)
    model_name = models.CharField(max_length=50, blank=True)
    make_year = models.CharField(max_length=5, blank=True)
    color = models.CharField(max_length=25, blank=True)
    job_description = models.TextField(blank=True)
    pickup_required = models.BooleanField(default=False)
    pickup_address = models.CharField(max_length=150, blank=True)
    pickup_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(Account, on_delete=models.RESTRICT, related_name='user_submitted')
    status = models.ForeignKey(JobStatus, on_delete=models.RESTRICT)
    staff = models.ForeignKey(Account, on_delete=models.RESTRICT, related_name='staff_assigned', limit_choices_to={'is_staff': True}, blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True,)
    updated_at  = models.DateTimeField(auto_now = True)
    
    REQUIRED_FIELDS = ['brand_name', 'model_name', 'make_year', 'color', 'job_description']
    
    def __str__(self) -> str:
        return self.job_id

class JobSparePart(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.RESTRICT, related_name='job_related', blank=True, null=True)
    spare_part_id = models.ForeignKey(Spareparts, on_delete=models.RESTRICT, related_name='Sparepart_assigned', blank=True, null=True)
    qty = models.IntegerField(default=1)
    cost_per_unit = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    staff = models.ForeignKey(Account, on_delete=models.RESTRICT, related_name='staff', limit_choices_to={'is_staff': True}, blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True,)
    updated_at  = models.DateTimeField(auto_now = True)
    
    REQUIRED_FIELDS = ['spare_part_id', 'qty', 'cost_per_unit']
    
    def __str__(self) -> str:
        return str(self.spare_part_id)
