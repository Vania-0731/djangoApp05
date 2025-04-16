from rest_framework import serializers
from .models import Category, Author, AuthorProfile, Publisher, Book, Publication

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AuthorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorProfile
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    profile = AuthorProfileSerializer(read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date', 'death_date', 'is_alive', 'profile']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    categories = CategorySerializer(many=True)
    publishers = PublisherSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
