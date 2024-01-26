from django.db import models
from account.models import Account
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
    user = models.ForeignKey(Account, on_delete=models.RESTRICT, related_name='user_submitted')
    status = models.ForeignKey(JobStatus, on_delete=models.RESTRICT)
    staff = models.ForeignKey(Account, on_delete=models.RESTRICT, related_name='staff_assigned', blank=True)
    created_at  = models.DateTimeField(auto_now_add=True,)
    updated_at  = models.DateTimeField(auto_now = True)
    
    REQUIRED_FIELDS = ['brand_name', 'model_name', 'make_year', 'color', 'job_description']
    
    def __str__(self) -> str:
        return self.job_id
