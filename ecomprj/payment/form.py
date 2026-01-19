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
            'delivery_country'
        ]
        exclude = ['user']