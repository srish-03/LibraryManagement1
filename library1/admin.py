from django.contrib import admin
from .models import Book,IssuedBook,Student

# Register your models here.

admin.site.register([Book,IssuedBook,Student])