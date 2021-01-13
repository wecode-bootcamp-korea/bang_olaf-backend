from django.db      import models
from user.models    import Users
from product.models import Products

class Payments(models.Model):
    order          = models.OneToOneField("Orders", on_delete=models.CASCADE)
    user           = models.ForeignKey(Users, on_delete=models.CASCADE)
    card           = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    created_at     = models.DateField(auto_now_add=True)
    updated_at     = models.DateField(auto_now=True) 
    class Meta:
        db_table = 'payments'

class Orders(models.Model):
    user       = models.ForeignKey(Users, on_delete=models.CASCADE)
    status     = models.ForeignKey("Status", on_delete=models.CASCADE)
    payment    = models.ForeignKey("Payments", on_delete=models.CASCADE)
    address    = models.ForeignKey("Address", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'orders'

class Status(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'status'

class Carts(models.Model):
    order        = models.ForeignKey("Payments", on_delete=models.CASCADE)
    product      = models.ForeignKey(Products, on_delete=models.CASCADE)
    count        = models.IntegerField(default=1)
    giftwrapping = models.BooleanField()

    class Meta:
        db_table = 'carts'

class GiftWrapping(models.Model):
    cart           = models.ForeignKey("Carts", on_delete=models.CASCADE,related_name="cart")
    edition_gold   = 'Gold'
    edition_silver = 'Silver'

    edition_choies = [
		(edition_gold, 'Gold'),
        (edition_silver, 'Silver')
    ]
    edition     = models.CharField(max_length=6, choices=edition_choies, default=edition_gold)
    description = models.TextField()

    class Meta:
        db_table = 'giftwrapping'

class Address(models.Model):
    name    = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email   = models.EmailField(max_length=254)

    class Meta:
        db_table = 'address'