from django.shortcuts import render

from django.views     import View
from django.http      import JsonResponse

from product.models   import Category, Product, Main, SubCategory

# mainpage
class MainPageView(View):
    def get(self, request, product_id):

        responses     = {}

        # 카테고리(스피커, 헤드폰, TV, 액세서리) 가져오는 부분
        categories    = Category.objects.all()
        categories_id = []

        for category in categories:
            categories_id.append(category.id)

        # 상품 (이미지, 타이틀, 설명) 가져오는 부분
        product           = Product.objects.get(id = product_id)
        informations      = Main.objects.filter(product = product)

        main_images       = []
        main_titles       = []
        main_descriptions = []

        for information in informations:
            main_images.append(information.mainimage_url)
            main_titles.append(information.title)
            main_descriptions.append(information.description)

        responses['product_images']       = product_images
        responses['product_titles']       = product_titles
        responses['product_descriptions'] = product_descriptions

        return JsonResponse(responses, status=200)

# product_list_page

class ProductListPageView(View):
    def get(self, request, category_id):

        category         = Category.objects.get(id = category_id)
        subcategies      = SubCategory.objects.filter(category = category)

        responses        = {}
        subcategories_id = []
        products         = []
        
        for subcategory in subcategies:
            subcategories_id.append(subcategory.id)
            products.append(Product.objects.filter(sub_category=sub_category))

        responses = {
            'subcategories_id' = subcategories_id,
            'products'         = products
        }

        return JsonResponse(responses, status = 200)



    

        

            


       



         

        










        