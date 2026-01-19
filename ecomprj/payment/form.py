from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):

    shipping_full_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    shipping_phone_number = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    shipping_email = forms.CharField(label='',widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    shipping_address_line1 = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 1'}))
    shipping_address_line2 = forms.CharField(label='',required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 2 (Optional)'}))
    shipping_city = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}))
    shipping_state = forms.CharField(label='',required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State (Optional)'}))
    shipping_zip_code = forms.CharField(label='',required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code (Optional)'}))
    shipping_country = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}))                   

    class Meta:
        model = ShippingAddress
        fields = [
            'shipping_full_name',
            'shipping_phone_number',
            'shipping_email',
            'shipping_address_line1',
            'shipping_address_line2',
            'shipping_city',
            'shipping_state',
            'shipping_zip_code',
            'shipping_country'
        ]
        exclude = ['user']