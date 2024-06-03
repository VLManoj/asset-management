from rest_framework import viewsets
from .models import AssetCategory
from .serializers import AssetCategorySerializer

class AssetCategoryViewSet(viewsets.ModelViewSet):
    queryset = AssetCategory.objects.all()
    serializer_class = AssetCategorySerializer
