from django.shortcuts import render

from rest_framework import viewsets
from .models import Books
from .serializers import BookSerializer

# Create your views here.

class BooksApiViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer