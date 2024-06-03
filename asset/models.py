from django.db import models

class AssetCategory(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=10)
