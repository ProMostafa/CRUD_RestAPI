from django.urls import path ,include
from .views import AricleViewSet
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('article',AricleViewSet,basename="viewset")

urlpatterns = [
    path("viewset/",include(router.urls)),
    path("viewset/<int:pk>/",include(router.urls)),
]
