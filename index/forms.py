from django import forms
from Publication.models import *
from Consultion.models import *
from Contact.models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__' 

class ConsultionForm(forms.ModelForm):
    class Meta:
        model = Consultion
        fields = '__all__' 


class PaymentForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'