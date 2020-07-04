from django.shortcuts import render
from rest_framework.response import Response
from .models import Article
from .serializer import ArticleSerializer
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# Create your views here.



class AricleViewSet(viewsets.ViewSet):

    def list(self, request):
        articles=Article.objects.all()
        serializer=ArticleSerializer(articles,many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        queryset=Article.objects.all()
        article=get_object_or_404(queryset,pk=pk)
        serializer=ArticleSerializer(article)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset=Article.objects.all()
        article=get_object_or_404(queryset,pk=pk)
        serializer=ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        
    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        Article.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_202_ACCEPTED)
