from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'categories'

class SubCategories(models.Model):
    category = models.ForeignKey("Categories", on_delete=models.CASCADE)
    name     = models.CharField(max_length=50)

    class Meta:
        db_table = 'subcategories'

class Products(models.Model):
    subcategory  = models.ForeignKey("SubCategories", on_delete=models.CASCADE)
    title        = models.CharField(max_length=50)
    detail_title = models.CharField(max_length=50)
    price        = models.DecimalField(max_digits=18, decimal_places=2) 
    description  = models.TextField()

    class Meta:
        db_table = 'products'

class Mains(models.Model):
    product       = models.ForeignKey("Products", on_delete=models.CASCADE)
    title         = models.CharField(max_length=50)
    description   = models.CharField(max_length=50)
    mainimage_url = models.CharField(max_length=100)

    class Meta:
        db_table = 'mains'
    

class Services(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'services'

class ProductServices(models.Model):
    product = models.ForeignKey("Products", on_delete=models.CASCADE)
    service = models.ForeignKey("Services", on_delete=models.CASCADE)

    class Meta:
        db_table = 'productservices'



class ProductColors(models.Model):
    product = models.ForeignKey("Products", on_delete=models.CASCADE)
    color   = models.ForeignKey("Colors", on_delete=models.CASCADE)

    class Meta:
        db_table = 'productcolors'

class Colors(models.Model):
    name               = models.CharField(max_length=50)
    image_url          = models.CharField(max_length=200)

    class Meta:
        db_table = 'colors'

class ColorImages(models.Model):
    colorimage_url = models.CharField(max_length=200)
    productcolor   = models.ForeignKey("ProductColors", on_delete=models.CASCADE)

    class Meta:
        db_table = 'colorimages'

class Products_Specifications(models.Model):
    product           = models.ForeignKey("Products", on_delete=models.CASCADE)
    specifications    = models.ForeignKey("Specifications", on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_spec'

class Specifications(models.Model):
    name = models.CharField(max_length=50)
    data = models.JSONField()

    class Meta:
        db_table = 'specifications'

class Inspirations(models.Model):
    title            = models.CharField(max_length=50)
    description      = models.TextField()
    video_url        = models.CharField(max_length=200)
    slide_image_url  = models.CharField(max_length=200)

    class Meta:
        db_table = 'inspirations'


class Features(models.Model):
    image_url    = models.CharField(max_length=200)
    video_url    = models.CharField(max_length=200)
    description  = models.TextField()
    title        = models.CharField(max_length=50)
    subtitle     = models.CharField(max_length=50)

    class Meta:
        db_table = 'features'