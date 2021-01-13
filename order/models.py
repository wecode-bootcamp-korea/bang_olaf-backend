from django.db      import models

from user.models    import User

from product.models import Product

class Payment(models.Model):
    order          = models.OneToOneField("Order", on_delete=models.CASCADE, null=True)
    card           = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    ammount        = models.IntegerField(null=True)
    created_at     = models.DateField(auto_now_add=True)
    updated_at     = models.DateField(auto_now=True)    

    class Meta:
        db_table = 'payment'

class Order(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    status     = models.ForeignKey("Status", on_delete=models.CASCADE)
    address    = models.ForeignKey("Address", on_delete=models.CASCADE, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'order'

class Status(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'status'

class Cart(models.Model):
    order         = models.ForeignKey("Order", on_delete=models.CASCADE)
    product       = models.ForeignKey(Product, on_delete=models.CASCADE)
    count         = models.IntegerField(default=1)
    gift_wrapping = models.BooleanField()

    class Meta:
        db_table = 'cart'

class GiftWrapping(models.Model):
    EDITION_GOLD    = 'Gold'
    EDITION_SILVER  = 'Silver'

    EDITION_CHOICES = [
		(EDITION_GOLD, 'Gold'),
        (EDITION_SILVER, 'Silver')
    ]
    edition     = models.CharField(max_length=6, choices=EDITION_CHOICES, default=EDITION_GOLD)
    description = models.TextField()
    cart        = models.ForeignKey("Cart", on_delete=models.CASCADE,related_name="cart")

    class Meta:
        db_table = 'giftwrapping'

class Address(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'address'