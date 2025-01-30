from django.db import models
from django.views.generic import TemplateView

# Create your models here.
class MenuView(TemplateView):
    template_name='orders/menu.html'

class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    is_avaialble=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS_CHOICES=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('ready', 'Ready'),
        ('completed', 'Completed')
    ]
    customer_name=models.CharField(max_length=200)
    customer_email=models.EmailField()
    created_at=models.DateTimeField(auto_now_add=True)
    pickup_time=models.DateTimeField()
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount=models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"order {self.id} - {self.customer_name}"
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantity}x {self.product.name}"
    
    