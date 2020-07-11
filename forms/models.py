from django.db import models

# Create your models here.
class accident(models.Model):
    location = models.CharField(max_length = 100)
    description = models.TextField()
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    incident_location = models.TextField()
    intial_severity = models.CharField(max_length=100)
    suspected_cause = models.TextField()
    action_taken = models.TextField()
    sub_incident_types = models.TextField()