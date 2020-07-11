from django.shortcuts import render
from django.http import HttpResponse
from .models import accident


# Create your views here.
def index(request):
    return render(request, 'form.html')
def onSubmit(request):
    location = request.POST["location"]
    description = request.POST["description"]
    date = request.POST["date"] + " " + request.POST["time"]
    incident_location = request.POST["incident_location"]
    intial_severity = request.POST["intial_severity"]
    suspected_cause = request.POST["suspected_cause"]
    action_taken = request.POST["action_taken"]
    sub_incident_types = request.POST.getlist("checks")

    accident_submit = accident(location=location,description=description,date=date,incident_location=incident_location,intial_severity=intial_severity,suspected_cause=suspected_cause,action_taken=action_taken,sub_incident_types=sub_incident_types)
    accident_submit.save()
    return render(request, 'form.html')