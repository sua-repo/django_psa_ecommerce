from django.shortcuts import render, redirect
from django.contrib import messages

from cart.cart import Cart
from orders.models import Order, OrderItem
from store.models import Product

# Create your views here.


# dev_24
def create_orders(request):

    if request.POST:
        cart = Cart(request)

        if request.user.is_authenticated:  # 로그인 상태일 때만 주문 가능
            user = request.user

            # Order(주문) 생성 및 저장
            create_order = Order(user=user)
            create_order.amount_paid = cart.get_product_total()  # 총 결제 금액
            create_order.save()

            # OrderItem(주문 상품) 생성 및 저장
            order_id = create_order.pk  # 주문 ID

            for item in cart:
                print(item)

                create_order_item = OrderItem(
                    order_id=order_id,
                    product_id=item["product"].id,
                    quantity=item["quantity"],
                    price=item["price"],
                )
                create_order_item.save()

            # 만약 카트도 지우고 싶다면?
            cart_keys = list(cart.get_cart().keys())

            for product_id in cart_keys:
                product = Product.objects.get(id=product_id)
                cart.remove(product)

            messages.success(request, "주문이 완료되었습니다.")
            return redirect("/")

        else:
            messages.success(request, "주문을 위해서는 로그인을 하셔야 합니다.")
            return redirect("/")

    else:
        messages.success(request, "잘못된 접근입니다.")
        return redirect("/")
