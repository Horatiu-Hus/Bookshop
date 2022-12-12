from django.db import models
from django.templatetags.static import static


class SpecificationCategory(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)


class Specification(models.Model):
    class Meta:
        unique_together = ('specification_category', 'name')

    specification_category = models.ForeignKey(SpecificationCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=False, unique=False)
    value = models.CharField(max_length=255, null=False)


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, default=None, null=True)
    name = models.CharField(max_length=255, unique=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    specifications = models.ManyToManyField(Specification)
    image = models.ImageField(upload_to='products/', null=True, default=None)

    @property
    def image_url(self):
        if self.image.url:
            return self.image

        return static('images/book_image.png')

