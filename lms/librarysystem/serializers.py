# serializers.py

from rest_framework import serializers
from .models import User, Book, BookDetails, BorrowedBooks

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['UserID', 'Name', 'Email', 'MembershipDate']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['BookID', 'Title', 'ISBN', 'PublishedDate', 'Genre']

class BookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetails
        fields = ['DetailsID', 'Book', 'NumberOfPages', 'Publisher', 'Language']

class BorrowedBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBooks
        fields = ['UserID', 'BookID', 'BorrowDate', 'ReturnDate']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['UserID'] = instance.UserID.UserID
        representation['BookID'] = instance.BookID.BookID
        return representation
