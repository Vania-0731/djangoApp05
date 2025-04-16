from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación con el modelo User
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()

    def __str__(self):
        return self.title


class BookCopy(models.Model):
    book = models.ForeignKey(Book, related_name='copies', on_delete=models.CASCADE)
    available = models.BooleanField(default=True)  # Si está disponible para préstamo
    condition = models.CharField(max_length=100, default="Good")  # Condición del libro

    def __str__(self):
        return f"{self.book.title} ({'Available' if self.available else 'Not Available'})"


class Loan(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book_copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE)
    checkout_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    late_fee = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def calculate_late_fee(self):
        if self.return_date and self.return_date > self.due_date:
            days_late = (self.return_date - self.due_date).days
            self.late_fee = days_late * 0.5
        return self.late_fee

    def __str__(self):
        return f"Loan: {self.member.user.username} - {self.book_copy.book.title}"


class Reservation(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reservation_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Pending")  # Pending, Fulfilled, Cancelled

    def __str__(self):
        return f"Reservation: {self.member.user.username} - {self.book.title}"
