from django import forms

class TravelInfoForm(forms.Form):
    phone_number = forms.IntegerField(required=True)
    destination = forms.CharField(max_length=20,required=True)
    arrival_date = forms.DateField(required=True,widget=forms.DateInput)
    arrival_time = forms.TimeField(required=True,widget=forms.TimeInput)
    preferred_transport = forms.CharField(max_length=20,required=True)