from rest_framework import serializers
from .models import Order, OrderItem
from cartItem.models import CartItem

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'shippingaddress']

    def create(self, validated_data):
        user = validated_data['user']

        # Obtén todos los elementos del carrito para el usuario
        cart_items = CartItem.objects.filter(user=user)
        if not cart_items.exists():
            print(cart_items)
            raise serializers.ValidationError("No items in the cart to create an order.")
            

        # Calcula el precio total
        total_price = sum(item.product.price * item.quantity for item in cart_items)

        # Crea la orden
        order = Order.objects.create(
            user=user,
            total_price=total_price
        )

        # Crea los OrderItem a partir de los CartItem
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price = cart_item.product.price,
            )

        # Limpia el carrito
        cart_items.delete()

        return order


class PendingOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'status','total_price']