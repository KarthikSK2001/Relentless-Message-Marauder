# typing_app/forms.py
from django import forms
from .models import TypingData

class TypingDataForm(forms.ModelForm):
    class Meta:
        model = TypingData
        fields = ('sleep_time', 'count', 'text')
