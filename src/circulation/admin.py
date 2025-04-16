from django.contrib import admin
from .models import Member, Book, BookCopy, Loan, Reservation

admin.site.register(Member)
admin.site.register(Book)
admin.site.register(BookCopy)
admin.site.register(Loan)
admin.site.register(Reservation)
