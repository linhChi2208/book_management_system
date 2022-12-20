from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date, time, timedelta

# Create your models here.
class Author(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50, unique=True)
  birth_death_date = models.CharField(max_length=20)
  description = models.CharField(max_length=250, null=True)

  def __str__(self):
    return self.name  


class Categories(models.Model):
  id = models.AutoField(primary_key=True)
  nom = models.CharField(max_length=50)
  
  def __str__(self):
    return f'Categorie: {self.nom}'

BOOK_STATUS = (
  ('A', 'Available'),
  ('B', 'Borrowed')
)
class Book(models.Model):
  isbn = models.AutoField(primary_key=True)
  title = models.CharField(max_length=255)
  author = models.ForeignKey('Author', null=True, on_delete = models.SET_NULL)
  categorie = models.ForeignKey('Categories', null=True, on_delete = models.SET_NULL)
  keywords = models.CharField(max_length=100)
  status = models.CharField(max_length=20, choices=BOOK_STATUS, default='Available')

  def __str__(self):
    return self.title
    


GENDER_CHOICES = (
  ('M', 'Male'),
  ('F', 'Female')
)
class Borrower(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.OneToOneField(User, related_name='borrower', on_delete=models.CASCADE)
  gender = models.CharField(max_length=8, choices=GENDER_CHOICES, default='Male')


  def __str__(self):
    return self.user.username


class Loan(models.Model):
  borrower_id = models.ForeignKey('Borrower', on_delete = models.CASCADE)
  isbn = models.ForeignKey('Book', on_delete = models.CASCADE)
  date_out = models.DateField(default=datetime.now())
  date_due = models.DateField(default = datetime.now() + timedelta(days=14))
  date_returned = models.DateField(null=True, blank=True)

  def __str__(self):
    return f'{self.borrower_id} {self.isbn} {self.date_out} {self.date_due} {self.date_returned}'
