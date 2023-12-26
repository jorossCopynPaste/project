from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class publicCategory(models.Model):
    class Meta:
        verbose_name = 'publicCategory'
        verbose_name_plural = 'publicCategories'

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class publicPhoto(models.Model):
    class Meta:
        verbose_name = 'publicPhoto'
        verbose_name_plural = 'publicPhotos'
    
    publiccategory = models.ForeignKey(
        publicCategory, on_delete=models.SET_NULL, null=True, blank=True)
    publicimage = models.ImageField(null=False, blank=False)
    publicdescription = models.TextField()

    def __str__(self):
        return self.publicdescription