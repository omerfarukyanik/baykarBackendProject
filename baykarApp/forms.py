from django import forms
from .models import RentalLog


class RentalLogForm(forms.ModelForm):
    class Meta:
        model = RentalLog
        fields = ['product', 'rental_amount', 'rental_unit_price']
