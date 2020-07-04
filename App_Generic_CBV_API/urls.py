

from django.urls import path ,include
from .views import GenericAPIView

urlpatterns = [
   path('article/', GenericAPIView.as_view(),name="article"),
   #the name paramter must be the same name using in view
   path('article/<int:id>', GenericAPIView.as_view(),name="details"),
]


