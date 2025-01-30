from rest_framework import serializers
from .models import Product, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id', 'name', 'description', 'price', 'is_available']
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields=['id', 'product', 'quantity', 'price']
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['id', 'customer_name', 'customer_email', 'pickup_time', 'status',
                'total_amount', 'items', 'created_at']
            