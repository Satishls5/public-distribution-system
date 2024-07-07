from django.db import models

class DistrictSupplyOfficer(models.Model):
    idnumber = models.CharField(max_length=20, primary_key=True)
    designation = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    phone = models.IntegerField()
    mail = models.CharField(max_length=255)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=12)

class ProductPrice(models.Model):
    product_name = models.CharField(max_length=30, primary_key=True)
    price = models.FloatField()

    def __str__(self):
        return self.product_name

class ShopDetails(models.Model):
    shopno = models.CharField(max_length=30, primary_key=True)
    district = models.CharField(max_length=40)
    taluk = models.CharField(max_length=50)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.shopno

class RationShopStocks(models.Model):
    rationshop = models.ForeignKey(ShopDetails, null=False, on_delete=models.CASCADE)
    date = models.DateField()
    productname = models.ForeignKey(ProductPrice, on_delete=models.CASCADE)
    quantity = models.FloatField()

class DistrictCollector(models.Model):
    id_number = models.CharField(max_length=20, primary_key=True)
    district = models.CharField(max_length=30)
    phone = models.IntegerField()
    mail = models.CharField(max_length=255)
    collector_name = models.CharField(max_length=30)
    password = models.CharField(max_length=12)

class RationShopOfficer(models.Model):
    id_number = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=30)
    shopno = models.ForeignKey(ShopDetails, on_delete=models.CASCADE)
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    phonenumber = models.IntegerField()
    mail = models.CharField(max_length=255)

class CardDetails(models.Model):
    card_number = models.IntegerField(primary_key=True)
    head_of_house = models.CharField(max_length=30)
    husband_or_father_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=250)
    total_member = models.IntegerField(max_length=2)
    shopno = models.ForeignKey(ShopDetails,on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    mail = models.CharField(max_length=255)

    

class CardEntitlement(models.Model):
    card_number = models.ForeignKey(CardDetails,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=30,  unique=True)
    required_quantity = models.FloatField()
    balance_quantity = models.FloatField()

class Transaction_histroy(models.Model):
    date = models.DateField()
    card_number = models.ForeignKey(CardDetails, on_delete=models.CASCADE)
    product_name = models.ForeignKey(ProductPrice, on_delete=models.CASCADE)
    quantity = models.FloatField(null=True)
    total_cost = models.FloatField()