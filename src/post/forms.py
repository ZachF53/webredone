from django import forms
from django.core.files import File


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        required=True, 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First and Last Name'
                }
        )
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Email'
                }
        )
    )
    service = forms.CharField( 
        required=True, 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'List the services your are interested in'
                }
        )
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea,
        )

class QuoteForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        required=True, 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First and Last Name',
                'rows': 1,
                'cols': 40
                }
        )
    )
    email = forms.EmailField(
        required=True,
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea,
        )


