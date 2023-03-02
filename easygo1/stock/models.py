from django.db import models

# Create your models here.

class Staff(models.Model):
  staffID = models.CharField(max_length=4, primary_key=True)
  staffName = models.TextField(null=True, blank=True)
  password = models.TextField(null=True, blank=True)

class Product(models.Model):
  productID = models.CharField(max_length=4, primary_key=True)
  productName = models.TextField()
  category = models.TextField()
  price = models.DecimalField(max_digits=4, decimal_places=2)
  totalQuantity = models.IntegerField(default=0)

class StocksManagement(models.Model):
  staffID = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
  productID = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
  date = models.DateField(null=True)
  quantity = models.IntegerField(null=True)
  status = models.CharField(max_length=3,null=True)

class AskQuestion(models.Model):
  staffID = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
  question = models.TextField()
  answer = models.TextField(null=True, blank=True, default='Pending')



