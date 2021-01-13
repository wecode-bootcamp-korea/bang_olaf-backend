from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'Category'

class SubCategory(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    name     = models.CharField(max_length=50)

    class Meta:
        db_table = 'subcategory'

class Product(models.Model):
    sub_category  = models.ForeignKey("SubCategory", on_delete=models.CASCADE)
    title        = models.CharField(max_length=50)
    detail_title = models.CharField(max_length=50)
    price        = models.DecimalField(max_digits=18, decimal_places=2) 
    description  = models.TextField()

    class Meta:
        db_table = 'product'

class Main(models.Model):
    product       = models.ForeignKey("Product", on_delete=models.CASCADE)
    title         = models.CharField(max_length=50)
    description   = models.CharField(max_length=50)
    main_image_url = models.CharField(max_length=100)

    class Meta:
        db_table = 'main'
    

class Service(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'service'

class ProductService(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    service = models.ForeignKey("Service", on_delete=models.CASCADE)

    class Meta:
        db_table = 'productservice'




class Color(models.Model):
    name               = models.CharField(max_length=50)
    image_url          = models.CharField(max_length=200)

    class Meta:
        db_table = 'color'

class ProductImage(models.Model):
    image_url      = models.CharField(max_length=200)
    product        = models.ForeignKey("Product", on_delete=models.CASCADE)
    color          = models.ForeignKey("Color", on_delete=models.CASCADE)

    class Meta:
        db_table = 'ProductImage'

class ProductsSpecification(models.Model):
    product           = models.ForeignKey("Product", on_delete=models.CASCADE)
    specifications    = models.ForeignKey("Specification", on_delete=models.CASCADE)

    class Meta:
        db_table = 'ProductsSpecification'

class Specification(models.Model):
    name = models.CharField(max_length=50)
    data = models.JSONField()

    class Meta:
        db_table = 'specification'

class Inspiration(models.Model):
    product          = models.OneToOneField("Product", on_delete=models.CASCADE)
    title            = models.CharField(max_length=50)
    description      = models.TextField()
    video_url        = models.CharField(max_length=200)
    slide_image_url  = models.CharField(max_length=200)

    class Meta:
        db_table = 'inspiration'


class Feature(models.Model):
    product      = models.OneToOneField("Product", on_delete=models.CASCADE)
    image_url    = models.CharField(max_length=200)
    video_url    = models.CharField(max_length=200)
    description  = models.TextField()
    title        = models.CharField(max_length=50)
    subtitle     = models.CharField(max_length=50)

    class Meta:
        db_table = 'feature'