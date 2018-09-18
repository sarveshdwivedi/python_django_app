from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from .models import Product, Order


def index(request):
    userdata = {
        'title': 'Sarvesh'
    }
    return render(request, "customer/index.html", {'userda': userdata})
#   return HttpResponse("Hello, world. You're at the polls index.")


def productdetail(request, product_id):
    print(product_id)
    ProductDetails = get_object_or_404(Product, pk=product_id)
    print(ProductDetails)
    print(ProductDetails.Name)
    return render(request, 'customer/details.html', {'Products': ProductDetails})


def productlists(request):
    product_list = Product.objects.order_by('-Created')[:5]
    # template = loader.get_template('polls/list.html')
    context = {
        'product_list': product_list,
    }
    return render(request, 'customer/list.html', context)

def orderdetail(request, order_id):
    print(order_id)
    OrderDetails = get_object_or_404(Order, pk=order_id)
    print(OrderDetails)
    return render(request, 'customer/orderdetails.html', {'Orders': OrderDetails})


def orderlists(request):
    order_list = Order.objects.order_by('-id')[:5]
    # template = loader.get_template('polls/list.html')
    context = {
        'order_list': order_list,
    }
    return render(request, 'customer/orderlist.html', context)    
