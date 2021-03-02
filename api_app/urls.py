from django.urls import include,path

from rest_framework import routers, views
from . import views

router = routers.DefaultRouter()
router.register('books',views.BooksApiViewSet)

urlpatterns = [
    path('',include(router.urls)),
]