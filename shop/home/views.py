from django.shortcuts import render


def Store(request):
    context={}
    return render (request,'store/store.html',context)



def Checkout(request):
    context={}
    return render (request,'store/checkout.html',context)



def Cart(request):
    context={}
    return render (request,'store/cart.html',context)



