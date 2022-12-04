from django.db import models

# Create your models here.

class Category(models.Model):
    parent      = models.ForeignKey('self',on_delete=models.CASCADE,related_name='children',blank=True,null=True)
    name        = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')


class Product(models.Model):
    name        = models.CharField(max_length=100, blank=True, null=True)
    price       = models.PositiveIntegerField(default=0)
    categories  = models.ManyToManyField(Category)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = ('Product')
        verbose_name_plural = ('Products')