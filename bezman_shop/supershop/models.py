from django.db import models

# Create your models here.
class Product(models.Model):
    types = (
        ('classic','classic'),
        ('sport','sport'),
        ('dm','demi-season'),
        ('winter','winter')
    )
    genders = (
        ('male','male'),
        ('female','female'),
        ('uni','uni')
    )
    sizes = (
        ('child','child'),
        ('medium','medium'),
        ('large','large'),
        ('XL','XL')
    )

    name = models.CharField(max_length=40)
    product_type = models.CharField(max_length=40,choices=types)
    genders = models.CharField(max_length=20,choices=genders)
    product_model = models.CharField(max_length=50)
    price = models.IntegerField()
    manufacture = models.CharField(max_length=15)
    size = models.CharField(max_length=20,choices=sizes),
    image = models.ImageField(blank=True,default='default.png')