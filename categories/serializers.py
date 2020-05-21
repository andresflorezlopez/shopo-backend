from .models import Categories
from rest_framework import serializers

class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Categories
    fields = ('id', 'name', 'description')