from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from asset.api import AssetCategoryViewSet, SubcategoryViewSet

router = routers.DefaultRouter()
router.register(r'subcategories', SubcategoryViewSet)
router.register(r'asset-categories', AssetCategoryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]