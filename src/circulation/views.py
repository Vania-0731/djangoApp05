from django.shortcuts import render, redirect
from .models import Book, BookCopy, Loan, Reservation
from .forms import LoanForm, ReservationForm


def loan_book(request):
    if request.method == "POST":
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loan_success')
    else:
        form = LoanForm()
    return render(request, 'circulation/loan_book.html', {'form': form})

def reserve_book(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')
    else:
        form = ReservationForm()
    return render(request, 'circulation/reserve_book.html', {'form': form})
