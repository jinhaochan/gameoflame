from django import forms

class suggestion(forms.Form):
    suggestion = forms.CharField(label='What weird stuff do you have in mind?', max_length=200)
