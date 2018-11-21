# --*-- coding: utf-8 --*--
from django import forms

class NameForm(forms.Form):
	Sequence = forms.CharField(required=True, widget=forms.Textarea)
