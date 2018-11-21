# --*-- coding: utf-8 --*--
from django import forms

class NameForm(forms.Form):
	Sequence = forms.CharField(required=True, widget=forms.Textarea)

class NameForm_2(forms.Form):
	Sequence_2 = forms.CharField(required=True, widget=forms.Textarea)
