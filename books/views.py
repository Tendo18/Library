from django.shortcuts import render
from rest_framework import generics     
from .models import *
from .serializers import *

# Create your views here.
#Category views
class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#book views
class BookAPIView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
   