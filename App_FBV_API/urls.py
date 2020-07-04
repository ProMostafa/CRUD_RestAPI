

from django.urls import path ,include
from .views import article_list ,article_detail

urlpatterns = [
   path('article/', article_list,name="article"),
   path('details/<int:pk>', article_detail,name="details"),
]
