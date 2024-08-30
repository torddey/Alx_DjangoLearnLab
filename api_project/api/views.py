from django.shortcuts import render 
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response


class BookViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

