from django import forms
from .models import Bill, BillingCompany

class NewBill(forms.Form):
    company = forms.ChoiceField(choices = BillingCompany.objects.all(), label="Choose a company")
    due_date = forms.DateField(label= "Due Date")
    payment_amount = forms.FloatField(label="Enter the amount of the bill")
    frequency = forms.ChoiceField(choices = Bill.frequency, label = 'Frequency of Payment')

