from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):

    # choices / pilihan 
    CATEGORIES = (
        (1, 'Console'),
        (2, 'Accessories'),
        (3, 'Game Disc'),
    )

    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    on_stock = models.PositiveIntegerField()
    category = models.PositiveIntegerField(choices= CATEGORIES)

    def __str__(self):
        return self.name

    @property
    def available(self):
        if self.on_stock > 0:
            return True
        else:
            return False

    @property
    # image utama
    def main_image(self):
        if self.images:
            return self.images.first()
        else:
            return None


    def get_discounted_price(self, rate):
        final_price = self.price - (self.price * (rate/100))
        return final_price


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products')
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name 

    # image1.product 
    # product.images 

