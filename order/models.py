from django.db      import models
from user.models    import Users
from product.models import Products

class Payments(models.Model):
    user       = models.ForeignKey(Users, on_delete=models.CASCADE)
    card       = models.CharField(max_length=50)
    createtime = models.DateField(auto_now_add=True)

class Orders(models.Model):
    status     = models.ForeignKey("Status", on_delete=models.CASCADE)
    payment    = models.ForeignKey("Payments", on_delete=models.CASCADE)
    address    = models.ForeignKey("Address", on_delete=models.CASCADE)

class Status(models.Model):
    name = models.CharField(max_length=50)

class Carts(models.Model):
    user         = models.ForeignKey(Users, on_delete=models.CASCADE)
    product      = models.ForeignKey(Products, on_delete=models.CASCADE)
    order        = models.ForeignKey("Payments", on_delete=models.CASCADE)
    count        = models.IntegerField(default=1)
    giftwrapping = models.BooleanField()

class GiftWrapping(models.Model):
    cart           = models.ForeignKey("Carts", on_delete=models.CASCADE,related_name="cart")
    edition_choies = (
		('Gold', 'Gold'),
        ('Silver', 'Silver')
    )
    edition     = models.CharField(max_length=6, choices=edition_choies)
    description = models.TextField()

class Address(models.Model):
    name    = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email   = models.EmailField(max_length=254)



