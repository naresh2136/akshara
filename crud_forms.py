
from django import forms
from crud.models import *

class ProjectEntryForm(forms.ModelForm):
    class Meta:
        model = ProjectEntry
        fields = '__all__'
