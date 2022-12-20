from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from app.models import Author, Book, Loan
from app.api.serializers import AuthorSerializer, BookSerializer, LoanSerializer

class AuthorList(generics.ListCreateAPIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer


class AuthorDetail(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  def get(self, request, pk):
    try:
      author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
      return Response({'error':'Author not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)

  def put(self, request, pk):
    try:
      author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
      return Response({'error':'Author not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = AuthorSerializer(author, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    author=Author.objects.get(pk=pk)
    author.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



class BookList(generics.ListCreateAPIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  queryset = Book.objects.all()
  serializer_class = BookSerializer



class BookDetail(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  def get(self, request, pk):
    try:
      book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
      return Response({'error':'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(book)
    return Response(serializer.data)

  def put(self, request, pk):
    try:
      book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
      return Response({'error':'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    book=Book.objects.get(pk=pk)
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class LoanList(APIView):

  def get(self, request):
    loans = Loan.objects.filter(date_returned=None)
    serializer = LoanSerializer(loans, many=True)
    return Response(serializer.data)

  # def post(self,request):
  #   serializer = LoanSerializer(data=request.data)
    
  #   # book = Book.objects.get(isbn=pk)
  #   if serializer.is_valid():
  #     my_dict=serializer.validated_data
  #     isbn=my_dict[-1][1].isbn
  #     print(f'my_dict {my_dict}')
  #     print(f'isbn {isbn}')

  #     serializer.save()
  #     return Response(serializer.data, status=status.HTTP_201_CREATED)
  #   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoanDetail(APIView):
  def get(self, request, pk):
    try:
      loan = Loan.objects.get(pk=pk)
    except Loan.DoesNotExist:
      return Response({'error':'loan not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = LoanSerializer(loan)
    return Response(serializer.data)


  def put(self, request, pk):
    try:
      book = Loan.objects.get(pk=pk)
    except Loan.DoesNotExist:
      return Response({'error':'Loan not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = LoanSerializer(book, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    loan=Loan.objects.get(pk=pk)
    loan.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)