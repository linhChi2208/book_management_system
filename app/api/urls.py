from django.urls import path, include
from app.api.views import AuthorList, AuthorDetail, BookList, BookDetail, LoanList, LoanDetail


urlpatterns = [
  path('books/list/', BookList.as_view(), name='book-list'),
  path('books/<int:pk>', BookDetail.as_view(), name='book_details'),
  path('authors/list/', AuthorList.as_view(), name='authors_list'),
  path('authors/<int:pk>', AuthorDetail.as_view(), name='author_details'),
  path('borrowed_books/list/', LoanList.as_view(), name='borrowed_books_list'),
  path('borrowed_books/<int:pk>', LoanDetail.as_view(), name='borrowed_book_detail'),
]