from django.urls import path
from . import views

urlpatterns = [
    path('loan/', views.loan_book, name='loan_book'),
    path('reserve/', views.reserve_book, name='reserve_book'),
    path('return/', views.return_book, name='return_book'),
    path('history/', views.borrowing_history, name='borrowing_history'),
]
