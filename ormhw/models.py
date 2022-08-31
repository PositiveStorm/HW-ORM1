from django.db import models

# Create your models here.
class Element(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200)
