
from django import forms
from .models import rescueApply, rescuePost
class rescueApplyform(forms.ModelForm):
    class Meta:
        model = rescueApply
        fields = ('experience',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['experience'].label = 'How many years have you worked as a rescuer'
        
class rescuePostForm(forms.ModelForm):
    class Meta:
        model = rescuePost
        fields = ('location', 'rescue_image', 'animalName', 'requester_contact', 'rescue_location', 'animal_condition')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].label = 'Location'
        self.fields['rescue_image'].label = 'Upload Image'
        self.fields['rescue_image'].required = False
        self.fields['animalName'].label = 'Upload Image'
        self.fields['requester_contact'].label = 'Add contact'
        self.fields['rescue_location'].label = 'Add Location'
        self.fields['animal_condition'].label = 'Current Condition of the animal'
        