from django.shortcuts import render
from catalog.models import Product
from orders.models import Order, OrderItem

# Create your views here.
def cart(request):
    
    if request.method == 'POST':

        productId = request.POST['id']
        qty = 1
        product = Product.objects.filter(id = productId)

        if request.user.is_authenticated:

            customer = request.user
            orderId = Order.objects.filter(customer=customer,complete=False)
            
            if orderId:
                for orderId in orderId:
                    for product in product:
                        try:
                            orderAvail = OrderItem.objects.get(product_id=productId)
                            orderAvail.quantity += qty 
                            orderAvail.save()
                        except:
                            orderItem = OrderItem.objects.create(product_id=productId,order=orderId,quantity=qty)
            else:
                order = Order.objects.create(customer=request.user, complete=False)

                for product in product:
                    orderItem = OrderItem.objects.create(product_id=productId,order=order,quantity=qty)


    if request.user.is_authenticated:
        customer = request.user
        orderId = Order.objects.filter(customer=customer,complete=False)

        for orderId in orderId:
            orderObject = OrderItem.objects.filter(order = orderId)

        context = {'orderItem':orderObject, 'order':orderId}

    return render(request, 'cart/cart.html',context) 