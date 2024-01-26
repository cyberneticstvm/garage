from django.db import models

# Create your models here.

class Callback(models.Model):
    name        = models.CharField(max_length=100, blank=True)
    mobile      = models.CharField(max_length=15, blank=True)
    service     = models.CharField(max_length=50, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now = True)
    
    def __str__(self) -> str:
        return self.name
