from django.contrib import admin
from app.models import Author, Categories, Book, Borrower, Loan
# Register your models here.
admin.site.register(Author)
admin.site.register(Categories)
admin.site.register(Book)
admin.site.register(Borrower)
admin.site.register(Loan)



