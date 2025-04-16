from django import forms
from .models import Loan, Reservation

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['member', 'book_copy', 'due_date']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['member', 'book', 'status']
