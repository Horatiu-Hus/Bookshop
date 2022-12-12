from django.shortcuts import render, Http404, get_object_or_404
from products.models import Product, Category


def show_all_products(request):
    price = request.GET.get('price')
    if price is None:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(price=price).all()

    return render(request, 'products/all_products.html', {
        'products': products,
    })


def show_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)


    return render(request, 'products/product.html', {
        'product': product
    })

def show_all_categories(request):
    page = request.GET.get('page', 1)

    cateogries = Category.objects.all()

    paginator = Paginator(cateogries, 10)
    paginated_categories = paginator.get_page(page)

    return render(request, 'products/all_categories.html', {
        'paginated_categories': paginated_categories,
    })

