from django.shortcuts import render
from .models import Product,Order
from django.http import JsonResponse

def Store(request):
    products = Product.objects.all()
    context={'products':products}
    return render (request,'store/store.html',context)



def Checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,create = Order.objects.get_or_create(customer=customer,complate=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order ={'order.get_cart_items':0,'order.get_cart_total':0}

    
    context={'items':items,'order':order}
    return render (request,'store/checkout.html',context)



def Cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,create = Order.objects.get_or_create(customer=customer,complate=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order ={'order.get_cart_items':0,'order.get_cart_total':0}

    
    context={'items':items,'order':order}
    return render (request,'store/cart.html',context)



def updateItm(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Actions',action)
    print('product',productId)
    return JsonResponse('Items was added',safe=False)