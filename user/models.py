from django.db import models

class Users(models.Model):
    email             = models.EmailField(max_length=254)
    password          = models.CharField(max_length=100)
    first_name        = models.CharField(max_length=50)
    last_name         = models.CharField(max_length=50)

    class Meta:
        db_table = 'users'
