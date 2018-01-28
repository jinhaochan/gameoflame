from django import forms

class suggestion(forms.Form):
    suggestion = forms.CharField(label='suggestion', max_length=200)
