from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from .models import Order, OrderItem


@login_required
def place_order(request):
    cart = Cart.objects.get(user=request.user)

    total_amount = sum(
        item.get_total_price() for item in cart.items.all()
    )

    # Create Order
    order = Order.objects.create(
        user=request.user,
        total_amount=total_amount,
        payment_method='COD'  # For now
    )

    # Create Order Items
    for item in cart.items.all():
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.discounted_price or item.product.price
        )

        # Reduce stock
        item.product.stock -= item.quantity
        item.product.save()

    # Clear cart
    cart.items.all().delete()

    return redirect('orders:order_success')

#backend logic
from rest_framework.views import APIView
from rest_framework.response import Response

class CreateOrderView(APIView):
    def post(self, request):
        cart = Cart.objects.get(user=request.user)
        order = Order.objects.create(user=request.user)

        total = 0
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
            total += item.quantity * item.product.price

        order.total_amount = total
        order.save()

        cart.items.all().delete()

        return Response({"message": "Order placed successfully"})
