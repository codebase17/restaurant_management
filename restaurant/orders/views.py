from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework import viewsets
from rest_framework.serializers import Serializer

from orders.models import Order, Product
from orders.serialisers import ProductSerializer, OrderSerializer

# Create your views here.
class MenuView(TemplateView):
    template_name='orders/menu.html'

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    Serializer_class=ProductSerializer
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class = OrderSerializer