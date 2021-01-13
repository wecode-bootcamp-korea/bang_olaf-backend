from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=50)


class SubCategories(models.Model):
    category = models.ForeignKey("Categories", on_delete=models.CASCADE)
    name     = models.CharField(max_length=50)


class Products(models.Model):
    subcategory = models.ForeignKey("SubCategories", on_delete=models.CASCADE)
    title        = models.CharField(max_length=50)
    detail_title = models.CharField(max_length=50)
    price        = models.DecimalField(max_digits=18, decimal_places=2) 
    description  = models.TextField()

class Mains(models.Model):
    product = models.ForeignKey("Products", on_delete=models.CASCADE)
    title   = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    mainimage_url = models.CharField(max_length=100)

    

class Services(models.Model):
    name = models.CharField(max_length=50)
    
class ProductServices(models.Model):
    product = models.ForeignKey("Products", on_delete=models.CASCADE)
    service = models.ForeignKey("Services", on_delete=models.CASCADE)


class ProductColors(models.Model):
    product = models.ForeignKey("Products", on_delete=models.CASCADE)
    color   = models.ForeignKey("Colors", on_delete=models.CASCADE)


class Colors(models.Model):
    name               = models.CharField(max_length=50)
    colorpickimage_url = models.CharField(max_length=200)


class ColorImages(models.Model):
    colorimage_url = models.CharField(max_length=200)
    productcolor   = models.ForeignKey("ProductColors", on_delete=models.CASCADE)


class Products_Spec(models.Model):
    product = models.ForeignKey("Products", on_delete=models.CASCADE)
    spec    = models.ForeignKey("Specifications", on_delete=models.CASCADE)


class Specifications(models.Model):
    name = models.CharField(max_length=50)
    data = models.JSONField(encoder="utf-8")


class Inspirations(models.Model):
    title            = models.CharField(max_length=50)
    description      = models.TextField()
    video_url        = models.CharField(max_length=200)
    slideimage_url   = models.CharField(max_length=200)


class Features(models.Model):
    imageurl     = models.CharField(max_length=200)
    video        = models.CharField(max_length=200)
    description  = models.TextField()
    title        = models.CharField(max_length=50)
    subtitle     = models.CharField(max_length=50)






