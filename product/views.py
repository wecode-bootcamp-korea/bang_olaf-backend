import json

from django.shortcuts import render
from django.views     import View
from django.http      import JsonResponse

from product.models   import Categories, Products, Mains

class MainPageView(View):
    def get(self, request):

        responses     = {}

        # 카테고리(스피커, 헤드폰, TV, 액세서리) 가져오는 부분
        categories    = Categories.objects.all()
        categories_id = []

        for category in categories:
            categories_id.append(category.id)

        # 상품 (이미지, 타이틀, 설명) 가져오는 부분
        products             = Mains.objects.filter(product_id = product_id)
        product_images       = []
        product_titles       = []
        product_descriptions = []

        for image in products:
            product_images.append(image.mainimage_url)
            product_titles.append(image.title)
            product_descriptions.append(image.description)

        responses['product_images']       = product_images
        responses['product_titles']       = product_titles
        responses['product_descriptions'] = product_descriptions

        return JsonResponse(responses, status=200)
        

            


       



         

        










        