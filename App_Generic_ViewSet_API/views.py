from django.shortcuts import render
from .models import Article
from .serializer import ArticleSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404



# Create your views here.

class AricleGenericViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=ArticleSerializer
    queryset=Article.objects.all()
