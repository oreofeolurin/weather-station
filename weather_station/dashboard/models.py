from django.db import models

# Create your models here.
class dashboard(models.Model):
    temperature = models.CharField(max_length=10, blank=True, null=True)
    Humidity = models.CharField(max_length=10, blank=True, null=True)
    pressure = models.CharField(max_length=10, blank=True, null=True)
    altitude = models.CharField(max_length=10, blank=True, null=True)
    lightInt = models.CharField(max_length=10, blank=True, null=True)
    lastUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"dashboard"

        
