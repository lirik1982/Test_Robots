from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    email = forms.EmailField(max_length=255)

    class Meta:
        model = Customer
        fields = '__all__'
