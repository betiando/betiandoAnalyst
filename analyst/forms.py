# In forms.py...
from django import forms

class ModelFormCSVFile(forms.Form):
    name = forms.CharField(max_length=255)
    csvfile = forms.FileField()
