from django.forms import ModelForm
from django import forms
from .models import Contact

class ContactForm(ModelForm):
    """ Contact form to collect the users questions """

    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(widget=forms.EmailInput(), label='Email Address')
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', max_length=300, widget=forms.Textarea())
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']