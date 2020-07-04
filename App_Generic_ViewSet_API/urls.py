from django.urls import path ,include
from .views import AricleGenericViewSet
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('article',AricleGenericViewSet,basename="viewset")

urlpatterns = [
     path("genericviewset/",include(router.urls)),
    path("genericviewset/<int:pk>/",include(router.urls)),
]
