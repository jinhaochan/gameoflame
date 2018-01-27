from django import forms

class form(forms.Form):
    suggestion = forms.CharField(label='suggestion', max_length=200)
