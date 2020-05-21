from django.shortcuts import render
from rest_framework import viewsets

from .serializers import CategoriesSerializer
from .models import Categories

# Create your views here.
class CategoriesViewSet(viewsets.ModelViewSet):
  queryset = Categories.objects.all().order_by('name')
  serializer_class = CategoriesSerializer
