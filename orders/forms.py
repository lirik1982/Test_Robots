from django import forms

from orders.models import Order


class NewOrderForm(forms.ModelForm):
    robot_serial = forms.CharField(max_length=5)
    customer = forms.IntegerField()

    class Meta:
        model = Order
        fields = ['robot_serial']
