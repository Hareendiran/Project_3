# forms.py
from django import forms
from .models import CustomTopic

class CustomContentForm(forms.ModelForm):
    class Meta:
        model = CustomTopic
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'placeholder': 'Enter custom content'}),
        }