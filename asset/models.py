from django.db import models

class AssetCategory(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=10)
    def __str__(self):
        return self.name
    
class Subcategory(models.Model):
    category = models.ForeignKey(AssetCategory, related_name='subcategories', on_delete=models.CASCADE)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')])

    def __str__(self):
        return self.name