from django.db      import models
from user.models    import User
from product.models import Product

class Payment(models.Model):
    order          = models.OneToOneField("Order", on_delete=models.CASCADE)
    user           = models.ForeignKey(User, on_delete=models.CASCADE)
    ammount        = models.IntegerField()
    card           = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    created_at     = models.DateField(auto_now_add=True)
    updated_at     = models.DateField(auto_now=True) 
    class Meta:
        db_table = 'payment'

class Order(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    status     = models.ForeignKey("Status", on_delete=models.CASCADE)
    address    = models.ForeignKey("Address", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'order'

class Status(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'status'

class Cart(models.Model):
    payment       = models.ForeignKey("Payment", on_delete=models.CASCADE)
    product       = models.ForeignKey(Product, on_delete=models.CASCADE)
    count         = models.IntegerField(default=1)
    gift_wrapping = models.BooleanField()

    class Meta:
        db_table = 'cart'

class GiftWrapping(models.Model):
    cart            = models.ForeignKey("Cart", on_delete=models.CASCADE,related_name="cart")
    EDITION_GOLD    = 'Gold'
    EDITION_SILVER  = 'Silver'

    EDITION_CHOICES = [
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