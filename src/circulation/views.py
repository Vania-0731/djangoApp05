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

def return_book(request):
    loan = Loan.objects.get(id=request.POST.get('loan_id'))
    loan.return_date = request.POST.get('return_date')
    loan.save()
    return redirect('borrowing_history')

def borrowing_history(request):
    loans = Loan.objects.filter(member=request.user.member)
    return render(request, 'circulation/borrowing_history.html', {'loans': loans})