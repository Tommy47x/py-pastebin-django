from django import forms
from .models import PasteText

class PasteTextForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Leave a comment here'}))

    class Meta:
        model = PasteText
        fields = ['text']