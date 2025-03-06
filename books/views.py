from django.shortcuts import render
from rest_framework import generics     
from .models import Books  
from .serializers import BooksSerializer

# Create your views here.
class BookAPIView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
   