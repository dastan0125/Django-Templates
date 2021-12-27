from django.shortcuts import render
from django.views.generic import DetailView

from web.models import Product

def index(request):
    return render(request, 'web/index.html')


def shop(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render(request, 'web/shop.html', context)


class ProductDetailsView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product/product_details.html'
    context_object_name = 'product'
