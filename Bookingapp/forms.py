from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type='date'

class Bookingform(forms.ModelForm):
    class Meta():
        model=Booking
        fields=[
            "customer_name",
            "customer_num",
            "customer_address",
            "rent_date",
            "return_date",
        ]
        
        widgets={
            "customer_name":forms.TextInput(attrs={"class":"form-control border border-warning mt-2","placeholder":"Enter your name ..."}),
            "customer_num":forms.TextInput(attrs={"class":"form-control border border-warning mt-2",'pattern':'[0-9]+','title':'Enter Numbers only 0-9 ',"placeholder":"Enter your number ..."}),
            "customer_address":forms.TextInput(attrs={"class":"form-control border border-warning mt-2","placeholder":"Enter your address ..."}),
            "rent_date":DateInput(),
            "return_date":DateInput()
        }