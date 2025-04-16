from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Author, AuthorProfile, Publisher, Book, Publication
from .serializers import *

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorProfileViewSet(viewsets.ModelViewSet):
    queryset = AuthorProfile.objects.all()
    serializer_class = AuthorProfileSerializer

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def categories_view(request):
    return render(request, 'library/category_list.html')

def category_detail_view(request, slug):
    return render(request, 'library/category_detail.html', {'slug': slug})
