from django import forms
from .models import accident


class accidentForm(forms.ModelForm):
    class Meta:
        model = accident
        fields = '__all__'

    def clean_location(self):
        location = self.cleaned_data['location']
        if location==None:
            raise forms.ValidationError("*Fields are required")
        return location

    def clean_description(self):
        description = self.cleaned_data['description']
        if description==None:
            raise forms.ValidationError("*Fields are required")
        return description 

    def clean_date(self):
        date = self.cleaned_data['date']
        if date==None:
            raise forms.ValidationError("*Fields are required")
        return date 

    def clean_initial_severity(self):
        intial_severity = self.cleaned_data['intial_severity']
        if intial_severity==None:
            raise forms.ValidationError("*Fields are required")
        return intial_severity 
        
        
    
