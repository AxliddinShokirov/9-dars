from django.db import models
from django.db import models, transaction
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


class Banner(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(upload_to='banners/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)
    title = models.TextField()
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name
class Gym(models.Model):
    name = models.CharField(max_length=255)
    title=models.TextField()
    image=models.ImageField(upload_to='meida/')

class Product(models.Model):
    name = models.CharField(max_length=255)
    title= models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()

    def __str__(self):
        return self.name   
class Info (models.Model):
    name = models.CharField(max_length=255)
    value = models.TextField()
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address = models.TextField()
    message = models.TextField()
    def __str__(self):
        return self.name
    
class ProductEnter(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='entries')
    quantity = models.IntegerField()
    old_quantity = models.IntegerField(blank=True, null=True)  # Allow null for new instances
    date = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

    def save(self, *args, **kwargs):
        with transaction.atomic():
            if not self.id:
                self.old_quantity = self.product.quantity
                self.product.quantity += int(self.quantity)
            else:
                try:
                    previous_entry = ProductEnter.objects.get(id=self.id)
                    quantity_diff = int(self.quantity) - previous_entry.quantity
                    self.product.quantity += quantity_diff
                    self.old_quantity = previous_entry.quantity
                except ObjectDoesNotExist:
                    # Handle case where the entry doesn't exist
                    pass
            self.product.save()
            super().save(*args, **kwargs)                        
