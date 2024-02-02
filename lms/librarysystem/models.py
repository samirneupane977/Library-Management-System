from django.db import models

# Create your models here.

class User(models.Model):
    UserID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=255)
    Email=models.EmailField(unique=True)
    MembershipDate=models.DateField()

    def __str__(self):
        return f"{self.UserID}"

class Book(models.Model):
    BookID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=13, unique=True)
    PublishedDate = models.DateField()
    Genre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.BookID}"

class BookDetails(models.Model):
    DetailsID = models.AutoField(primary_key=True)
    Book = models.OneToOneField(Book, on_delete=models.CASCADE)
    NumberOfPages = models.PositiveIntegerField()
    Publisher = models.CharField(max_length=255)
    Language = models.CharField(max_length=50)


class BorrowedBooks(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    BookID = models.ForeignKey(Book, on_delete=models.CASCADE)
    BorrowDate = models.DateField()
    ReturnDate = models.DateField(null=True, blank=True)

