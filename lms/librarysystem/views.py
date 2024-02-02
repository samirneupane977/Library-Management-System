from rest_framework import viewsets
from .models import User, Book, BookDetails, BorrowedBooks
from .serializers import UserSerializer, BookSerializer, BookDetailsSerializer, BorrowedBooksSerializer

#view for user CRUD operations
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'UserID'

#view for Book CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'BookID'

#view for BoookDetail CRUD operations
class BookDetailsViewSet(viewsets.ModelViewSet):
    queryset = BookDetails.objects.all()
    serializer_class = BookDetailsSerializer
    lookup_field = 'DetailsID'

#view for BorrowedBook CRUD operations
class BorrowedBooksViewSet(viewsets.ModelViewSet):
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer
    lookup_field = 'BookID'
