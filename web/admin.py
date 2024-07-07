from django.contrib import admin
from .models import DistrictSupplyOfficer
from .models import ProductPrice
from .models import ShopDetails
from .models import RationShopStocks
from .models import DistrictCollector
from .models import RationShopOfficer
from .models import CardDetails
from .models import CardEntitlement 
from .models import Transaction_histroy
# Register your models here.
admin.site.register(DistrictSupplyOfficer)
admin.site.register(ProductPrice)
admin.site.register(ShopDetails)
admin.site.register(RationShopStocks)
admin.site.register(DistrictCollector)
admin.site.register(RationShopOfficer)
admin.site.register(CardDetails)
admin.site.register(CardEntitlement)
admin.site.register(Transaction_histroy)