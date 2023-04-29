from django import forms
from .models import adoptionPost

class adoptionForm(forms.ModelForm):
    class Meta:
        model = adoptionPost
        fields = ('adoptText', 'adopt_image', 'adoptee_contact', 'animalName', 'adoptee_location')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['adoptText'].label = 'Write down desciption'
        self.fields['adoptee_contact'].label = 'Your contact'
        self.fields['adopt_image'].label = 'Upload Image'
        self.fields['adopt_image'].required = False
        self.fields['animalName'].label = 'Add Animal Name'
        self.fields['adoptee_location'].label = 'Add Location'
        

class adoptUpdateForm(forms.ModelForm):
    class Meta:
        model = adoptionPost
        fields = ['adoptText', 'adoptee_contact', 'adopt_image', 'adoptee_location', 'adoptState', 'animalName']

