from django import forms

from robots.models import Robot


class RobotForm(forms.ModelForm):
    serial = forms.CharField(max_length=5)
    model = forms.CharField(max_length=2)
    version = forms.CharField(max_length=2)
    created = forms.DateTimeField()

    class Meta:
        model = Robot
        fields = '__all__'
