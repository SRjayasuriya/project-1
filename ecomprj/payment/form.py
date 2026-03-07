from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):

    delivery_full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}), required=True)
    delivery_email = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}), required=True)
    delivery_address_line1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address Line 1'}), required=True)
    delivery_address_line2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address Line 2 (Optional)'}), required=False)
    delivery_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City'}), required=True)
    delivery_state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'State (Optional)'}), required=False)
    delivery_zip_code = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Zip Code (Optional)'}), required=False)
    delivery_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Country'}), required=True)
    delivery_phone = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}), required=False)
    class Meta:
        model = ShippingAddress
        fields = [
            'delivery_full_name',
            'delivery_email',
            'delivery_address_line1',
            'delivery_address_line2',
            'delivery_city',
            'delivery_state',
            'delivery_zip_code',
            'delivery_country',
            'delivery_phone'
        ]
        exclude = ['user']

class PaymentForm(forms.Form):

    card_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name on Card'}), required=True)
    card_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Card Number'}), required=True)
    card_exp_date = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Expiration Date'}), required=True)
    card_cvv_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'CVV Code'}), required=True)
    card_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Billing Address1'}), required=True)
    card_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Billing Address2(not neccessary)'}), required=False)
    card_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Billing City'}), required=True)
    card_state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Billing State'}), required=True)
    card_zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Billing Zipcode'}), required=True)
    card_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Billing Country'}), required=True)