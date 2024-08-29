from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name

class Product(models.Model):
    SKU = models.CharField(max_length=100)
    name = models.CharField(max_length=100,default="unknown")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def _str_(self):
        return self.SKU
    

class Shipment(models.Model):
    shipment_id = models.AutoField(primary_key=True)
    shipment_date = models.DateField(auto_now=True)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=6)
    customer = models.ForeignKey(User,on_delete=models.CASCADE)



class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_date = models.DateField(auto_now=True)
    payment_method = models.CharField(max_length=100)
    payment_reference_id = models.CharField(max_length=300)
    payment_transaction_id = models.CharField(max_length=300)
    payment_status = models.CharField(max_length=300,default="PENDING")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(User,on_delete=models.CASCADE)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
    shipment = models.ForeignKey(Shipment,on_delete=models.CASCADE)

class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)