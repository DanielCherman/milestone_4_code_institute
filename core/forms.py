from django import forms
from .models import ContactUs

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class': 'form-control', }
        self.fields['email'].widget.attrs = {'class': 'form-control', }
        self.fields['subject'].widget.attrs = {'class': 'form-control', }
        self.fields['message'].widget.attrs = {'class': 'form-control', }
