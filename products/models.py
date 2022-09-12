from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """ Class for the Category model """

    class Meta:
        """ Set verbose name """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ Class for the Product model """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    # User_wishlist taken from Very Academy Youtube Video
    # https://www.youtube.com/watch?v=OgA0TTKAtqQ
    user_wishlist = models.ManyToManyField(User, related_name='user_wishlist', blank=True)

    def __str__(self):
        return self.name
