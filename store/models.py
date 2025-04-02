from django.db import models

# Create your models here.


class Collection(models.Model):
    title = models.CharField(max_length=255)
    feature_products = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name='+')


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)


class Customer(models.Model):   
    MEMBERSHIP_PREMIUM = "pr"
    MEMBERSHIP_STANDARD = "st"
    MEMBERSHIP_FREE = "fr"
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_PREMIUM, 'Premium'),
        (MEMBERSHIP_STANDARD, 'Standard'),
        (MEMBERSHIP_FREE, 'Free'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=2, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_FREE)


class Order(models.Model):
    STATUS_PENDING = 'p'
    STATUS_COMPLETED = 'c'
    STATUS_FAILED = 'f'
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_FAILED, 'Returned'),
    ]
    place_at = models.DateTimeField(auto_now_add=True)
    PAYMENT_STATUS = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default=STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    Customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE)


class Cart(models.Model):
    created_at = models.DateField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
