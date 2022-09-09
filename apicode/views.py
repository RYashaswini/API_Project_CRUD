from django.shortcuts import render
from rest_framework.views import APIView
from .models import Article
from .serializer import ArticleSerializer
from rest_framework.response import Response
from rest_framework import status,viewsets,filters
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import generics

#from rest_framework.filters import SearchFilter, OrderingFilter


class ArticleAPIView(generics.ListCreateAPIView):
    
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #filter_backends = (SearchFilter, OrderingFilter)
    #search_fields = ('id','title', 'author','email','shipping','journal')

class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleSearch(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    


   


