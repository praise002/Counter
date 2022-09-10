from django import forms
from django.forms import ModelForm
from . models import Count


class CountForm(ModelForm):
    class Meta:
        model = Count
        fields = '__all__'
        label = {'text': ''}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 20, 'style': 'resize: None;'}),
        }
