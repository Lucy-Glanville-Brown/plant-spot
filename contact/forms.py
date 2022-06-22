from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(widget=forms.EmailInput(), label='Email Address')
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', max_length=300, widget=forms.Textarea())