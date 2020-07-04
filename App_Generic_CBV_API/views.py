from django.shortcuts import render
from rest_framework.response import Response
from .models import Article
from .serializer import ArticleSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins

# Create your views here.


class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,
                        mixins.CreateModelMixin,mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin,mixins.DestroyModelMixin):


    serializer_class=ArticleSerializer
    queryset=Article.objects.all()
    lookup_field = "id"
   # authentication_classes=[SessionAuthentication,BasicAuthentication]
   # authentication_classes=[TokenAuthentication]
    #permission_classes=[IsAuthenticated]
    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=None):
        return self.destroy(request,id)

