from django import forms
from .models import ContactUs, CustomerQuery

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

class QuoteForm(forms.ModelForm):
    class Meta:
        model = CustomerQuery
        fields = ['title', 'design_type', 'width', 'height', 'unit', 'description', 'sketch', ]

    def __init__(self, *args, **kwargs):
        super(QuoteForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {'class': 'form-control', }
        self.fields['design_type'].widget.attrs = {'class': 'form-control', }
        self.fields['unit'].widget.attrs = {'class': 'form-control', }
        self.fields['description'].widget.attrs = {'class': 'form-control', }
