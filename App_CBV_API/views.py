from django.shortcuts import render
from rest_framework.response import Response
from .models import Article
from .serializer import ArticleSerializer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.


class ArticleAPIView(APIView):
    #override get method
    def get(self,request):
        articles=Article.objects.all()
        serializer=ArticleSerializer(articles,many=True)
        return Response(serializer.data)
    #override post method
    def post(self,request):
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):

    def get_object(self,id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,id):
        article=Article.objects.get(id=id)
        serializer=ArticleSerializer(article)
        return Response(serializer.data)

    def put(self,request,id):
        article=Article.objects.get(id=id)
        serializer=ArticleSerializer( article,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        Article.objects.get(id=id).delete()
        return Response(status=status.HTTP_202_ACCEPTED)