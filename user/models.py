from django.db import models

# Create your models here.
class Users(models.Model):
    email             = models.EmailField(max_length=254)
    password          = models.CharField(max_length=100)
    checkpassword       = models.CharField(max_length=100)
    first_name        = models.CharField(max_length=50)
    last_name         = models.CharField(max_length=50)
    preferred_laguage = models.CharField(max_length=50)

    