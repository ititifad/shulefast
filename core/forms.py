# forms.py
from django import forms
from .models import *

class UserFeedbackForm(forms.ModelForm):
    class Meta:
        model = UserFeedback
        fields = ['name', 'feedback_text']


class SchoolFilterForm(forms.Form):
    name = forms.CharField(required=False, label='School Name')
    region = forms.ModelChoiceField(queryset=Region.objects.all(), required=False, label='Region')
    subcategory = forms.ModelChoiceField(queryset=SubCategory.objects.all(), required=False, label='Subcategory')
    location = forms.CharField(required=False, label='Location')