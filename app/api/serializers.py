from rest_framework import serializers
from app.models import *

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields ='__all__'


class LoanSerializer(serializers.ModelSerializer):
  class Meta:
    model = Loan
    fields ='__all__'