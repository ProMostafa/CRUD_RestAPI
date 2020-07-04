

from django.urls import path ,include
from .views import ArticleAPIView ,ArticleDetails

urlpatterns = [
   path('article/', ArticleAPIView.as_view(),name="article"),
   #the name paramter must be the same name using in view
   path('details/<int:id>', ArticleDetails.as_view(),name="details"),
]
