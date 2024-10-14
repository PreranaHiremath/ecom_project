from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order
from django.contrib.auth.decorators import login_required
# Create your views here.
# List all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

# View a single product
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

# Place an order for a product
@login_required
def place_order(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        order = Order.objects.create(
            user=request.user,
            product=product,
            quantity=quantity,
            total_price=product.price * quantity
        )
        return redirect('order_confirmation', pk=order.pk)
    return render(request, 'shop/place_order.html', {'product': product})
