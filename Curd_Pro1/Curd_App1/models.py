from django.db import models

class Product(models.Model):
    Product_Number =models.IntegerField()
    Product_Name = models.CharField(max_length=60)
    Product_Cost = models.IntegerField()
    Product_Color = models.CharField(max_length=50)
    Product_Class =models.CharField(max_length=50)
    Number_Of_Products =models.IntegerField()
    Customer_Name = models.CharField(max_length=50)
    Customer_Number = models.BigIntegerField()
    Email_Id =models.EmailField(max_length=80)
