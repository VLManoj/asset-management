from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import AssetCategory, Subcategory
from .serializers import AssetCategorySerializer, SubcategorySerializer

class AssetCategoryViewSet(viewsets.ModelViewSet):
    queryset = AssetCategory.objects.all()
    serializer_class = AssetCategorySerializer

class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
