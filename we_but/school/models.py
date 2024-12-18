from django.db import models


class Task(models.Model):
    title=models.CharField( max_length=200)
    completed=models.BooleanField(default=False)


class Product(models.Model):
 name = models.CharField(max_length=100)
 price = models.DecimalField(max_digits=10, decimal_places=2)
 stock = models.PositiveIntegerField()
 description = models.TextField()
 
 def __str__(self):
    return self.name

class person(models.Model):
    name=models.CharField(max_length=100)
    age = models.IntegerField()

class employee(person):
    job_title = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

class TimestampedModel(models.Model):
    create_at=models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now_add=True)


class Meta:
   abstract = True

class Product_1(TimestampedModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
 
class Order(TimestampedModel):
   order_number = models.CharField(max_length=20)
   customer_name = models.CharField(max_length=100)

class Product_2(models.Model):
 name = models.CharField(max_length=100)
 price = models.DecimalField(max_digits=10, decimal_places=2)

class DiscountedProduct(Product_2):
 class Meta:
   proxy = True
   ordering = ['-price']