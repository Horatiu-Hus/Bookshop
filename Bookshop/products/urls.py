from django.urls import path
from products.views import show_all_products, show_product

app_name = 'products'

urlpatterns = [
    path('', show_all_products, name='all_products'),    #products/
    path('<int:product_id>/', show_product, name='products_details'),    #products/<int:product_id>
]