from django import forms


class TicketForm(forms.Form):
    name = forms.CharField(min_length=2)
    email = forms.EmailField()
    phone = forms.CharField(min_length=11, max_length=11)