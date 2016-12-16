from django import forms


class MonthForm(forms.Form):
    month = forms.CharField(max_length=10)
