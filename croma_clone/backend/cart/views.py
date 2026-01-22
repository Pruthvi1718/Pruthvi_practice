from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Cart, CartItem
from rest_framework.views import APIView
from rest_framework.response import Response

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
    cart_item.save()

    return redirect('cart:cart_detail')


@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)

    total = sum(item.get_total_price() for item in cart.items.all())

    return render(request, 'cart/cart_detail.html', {
        'cart': cart,
        'total': total
    })


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart:cart_detail')

#backend logic
class AddToCartView(APIView):
    def post(self, request):
        product_id = request.data.get('product_id')
        product = Product.objects.get(id=product_id)

        cart, _ = Cart.objects.get_or_create(user=request.user)
        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product
        )

        if not created:
            item.quantity += 1
        item.save()

        return Response({"message": "Added to cart"})
