from django.shortcuts import render, redirect, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from .models import DistrictSupplyOfficer
from .models import ProductPrice
from .models import ShopDetails
from .models import RationShopStocks
from .models import DistrictCollector
from .models import RationShopOfficer
from .models import CardDetails
from .models import CardEntitlement 
from .models import Transaction_histroy
# Create your views here.




#District Supply Officer

def register(request):
    if request.method == 'POST':
        member = DistrictSupplyOfficer(username=request.POST['username'], password=request.POST['password'],  idnumber=request.POST['userid'], designation=request.POST['designation'], district=request.POST['district'], phone=request.POST['phone'], mail=request.POST['mail'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'web/Register.html')

def login(request):
    return render(request, 'web/login.html')

def home(request):
    if request.method == 'POST':
        if DistrictSupplyOfficer.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = DistrictSupplyOfficer.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'web/home.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'web/login.html', context)
    return render(request,'web/home.html')
        
def addprice(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        price = request.POST['price']

        obj1 = ProductPrice()
        obj1.product_name = product_name
        obj1.price = price
        obj1.save()
        mydata=ProductPrice.objects.all()
        return render(request,'web/AddPrice.html',{'datas':mydata})
    return render(request,'web/AddPrice.html')

def pricelist(request):
    mydata=ProductPrice.objects.all()
    if(mydata!=''):
        return render(request,'web/PriceList.html',{'datas':mydata})
    else:
        return render(request,'web/PriceList.html')
    
def shopregister(request):
  
    if request.method == 'POST':
        shopno = request.POST['shop_number']
        district = request.POST['district']
        taluk = request.POST['taluk']
        location = request.POST['location']

        object_of_shop = ShopDetails()
        object_of_shop.shopno = shopno
        object_of_shop.district = district
        object_of_shop.taluk = taluk
        object_of_shop.location = location
        try:
            object_of_shop.save()
        except:
            context = {'msg': 'This Shop Details Already Registered '}
            return render(request, 'web/RationShops.html', context)        
        shopdata=ShopDetails.objects.all()
        return render(request,'web/RationShops.html',{'dataofshop':shopdata})
    return render(request,'web/RationShops.html')


def shoplist(request):
    shopdata=ShopDetails.objects.all()
    if(shopdata!=''):
        return render(request,'web/shoplist.html',{'dataofshop':shopdata})
    else:
        return render(request,'web/shoplist.html')

def shopstock(request):
    stockdata=RationShopStocks.objects.all()
    if(stockdata!=''):
        return render(request,'web/stocklist.html',{'dataofstock':stockdata})
    else:
        return render(request,'web/stocklist.html')


def addshopstock(request):
    if request.method == 'POST':
        rationshop = request.POST['rationshop']
        date = request.POST['date']
        product_name = request.POST['productname']
        quantity = request.POST['quantity']

        


        try:
            shop_instance = ShopDetails.objects.get(shopno=rationshop)
            stock_instance = ProductPrice.objects.get(product_name=product_name)
        except ShopDetails.DoesNotExist:
            context = {'msg': 'Shop number does not exist'}
            return render(request, 'web/stocklist.html', context)
        except ProductPrice.DoesNotExist:
            context = {'msg': 'Product does not exist'}
            return render(request, 'web/stocklist.html', context)

        object_of_StockDetails = RationShopStocks(
            rationshop=shop_instance,
            date=date,
            productname=stock_instance,
            quantity=quantity,
        )

        try:
            object_of_StockDetails.save()
            
            stockdata = RationShopStocks.objects.all()
            if stockdata != '':
                return render(request, 'web/stocklist.html', {'dataofshop': stockdata})
            

            # Fetching email addresses of all ration card members
            try:
                
                # mail = CardDetails.objects.values_list('mail', flat=True)


                # Sending email to all ration card members
                subject = 'New Stock Added'
                # message = f'Hello,\nNew stock of {product_name} - {quantity} has been added to the shop.'
                # send_mail(subject, message, 'soniyamanilax2@gmail.com', 'ragupalani2002@gmail.com')
            except:
                context = {'msg': 'Mail Not Sent!'}
                return render(request, 'web/stocklist.html',{'dataofstock':stockdata} ,context)

        except:
            context = {'msg': 'This Details Already Entered!'}
            return render(request, 'web/stocklist.html',{'dataofstock' : stockdata} , context)

        
        if stockdata != '':
            return render(request, 'web/stocklist.html', {'dataofshop': stockdata})
    return render(request, 'web/stocklist.html',{'dataofshop': stockdata})

def shopstocklist(request):
    stockdata=RationShopStocks.objects.all()
    if(stockdata!=''):
        return render(request,'district_collector/stock_list.html',{'dataofstock':stockdata})
    else:
        return render(request,'district_collector/stock_list.html')


def update_stock(request,id):
    stockdata = get_object_or_404(RationShopStocks, id=id)

    if request.method == 'POST':
        
        date = request.POST.get('date')
        quantity = request.POST.get('quantity')
        
        stockdata.date = date
        stockdata.quantity = quantity
        stockdata.save()

    return render(request,'web/updatestock.html',{'data': stockdata})
   
def update_price(request, product_name):
    pricedata = get_object_or_404(ProductPrice, product_name=product_name)

    if request.method == 'POST':
        updated_price = request.POST.get('price')
        pricedata.price = updated_price
        pricedata.save()

    return render(request, 'web/updateprice.html', {'data': pricedata})

def entitle_list(request):
    mydata=CardEntitlement.objects.all()
    if(mydata!=''):
        return render(request,'web/entitle_list.html',{'datas':mydata})
    else:
        return render(request,'web/entitle_list.html',{'datas':mydata})

def update_remaining_stock(request,id):
    stockdata = get_object_or_404(CardEntitlement, id=id)

    if request.method == 'POST':
        quantity = request.POST.get('re_quantity')
        
        stockdata.balance_quantity = quantity
        try:
            stockdata.save()
        except:
            context = {'msg': 'Cannot update the stock !'}
            return render(request,'web/entitle_update.html',context)

    return render(request,'web/entitle_update.html',{'data': stockdata})

#############################################################################################

def rationcard_details(request):
    if request.method == 'POST':
        card_no = request.POST['cardnumber']
        name = request.POST['name']
        father_or_husband_name = request.POST['co_name']
        date_of_birth = request.POST['date']
        address = request.POST['address']
        tot_member = request.POST['total_members']
        shop_no = request.POST['shop_no']
        phoneno = request.POST['phone']
        mail = request.POST['mail']

        if len(phoneno)==10:
            phoneno=phoneno
        else:
            context = {'msg': 'Phone is not valid !'}
            return render(request, 'web/e_card.html',context)

        try:
            shop_instance = ShopDetails.objects.get(shopno=shop_no)
        except ShopDetails.DoesNotExist:
            context = {'msg': 'Shop number does not exist'}
            return render(request, 'web/e_card.html', context)

        object_of_CardDetails = CardDetails(
            card_number=card_no,
            head_of_house=name,
            husband_or_father_name=father_or_husband_name,  
            date_of_birth=date_of_birth,
            address=address,
            total_member =tot_member,
            mail=mail,
            shopno=shop_instance,
            phone_number=phoneno,

        )

        try:
            object_of_CardDetails.save()
        except:
            context = {'msg': 'This Card Details Already Registered'}
            return render(request, 'web/e_card.html', context)

        carddata = RationShopOfficer.objects.all()
        return render(request, 'web/e_card.html', {'dataofshop': carddata})

    return render(request, 'web/e_card.html')

def entitlement(request):
    if request.method == 'POST':
        card_number = request.POST['card_number']
        productname = request.POST['product_name']
        required_quantity = request.POST['required_quantity']
        product_name = productname.capitalize()

        try:
            card_instance = CardDetails.objects.get(card_number=card_number)
        except CardDetails.DoesNotExist:
            context = {'msg': 'This Ration Card Number did not registered!'}
            return render(request, 'web/card_entitlement.html', context)
        
        balance_quantity = required_quantity

        object_of_Entitlement = CardEntitlement(
            card_number=card_instance,
            product_name=product_name,
            required_quantity=required_quantity,  
            balance_quantity=balance_quantity,

        )

        try:
            object_of_Entitlement.save()
        except:
            context = {'msg': 'This Product Details Already Entered'}
            return render(request, 'web/card_entitlement.html', context)

        carddata = CardEntitlement.objects.all()
        return render(request, 'web/card_entitlement.html', {'dataofshop': carddata})

    return render(request, 'web/card_entitlement.html')


#############################################################################################

#District Collector
def collector_register(request):
    if request.method == 'POST':
        member = DistrictCollector(collector_name=request.POST['collector_name'], password=request.POST['password'],  id_number=request.POST['userid'], district=request.POST['district'], phone=request.POST['phone'], mail=request.POST['mail'])
        member.save()
        return render(request,'district_collector/collector_login.html')
    else:
        return render(request, 'district_collector/collector_register.html')
    
def collector_login(request):
    if request.method == 'POST':
        collector_name = request.POST.get('collector_name')
        password = request.POST.get('password')
        try:
            user=DistrictCollector.objects.get(name = collector_name , password=password)
        except DistrictCollector.DoesNotExist:
            user = None
        if user is not None:
            return redirect('district_collector/collector_index.html')
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'district_collector/collector_login.html', context)
    return render(request,'district_collector/collector_login.html')

def collector_index(request):
    
    return render(request,'district_collector/index.html')

def collector_pricelist(request):
    mydata=ProductPrice.objects.all()
    if(mydata!=''):
        return render(request,'district_collector/price_list.html',{'datas':mydata})
    else:
        return render(request,'district_collector/price_list.html')
    
def collector_shoplist(request):
    shopdata=ShopDetails.objects.all()
    if(shopdata!=''):
        return render(request,'district_collector/shop_list.html',{'dataofshop':shopdata})
    else:
        return render(request,'district_collector/shop_list.html')
    
def collector_stocklist(request):
    stockdata=RationShopStocks.objects.all()
    if(stockdata!=''):
        return render(request,'district_collector/stock_list.html',{'dataofstock':stockdata})
    else:
        return render(request,'district_collector/stock_list.html')
    
###################################################################################

#Ration Shop Officer
def rationshop_officer_register(request):
    if request.method == 'POST':
        R_userid = request.POST['r_userid']
        R_number = request.POST['ration_shop_no']
        R_officername = request.POST['officer_name']
        R_password = request.POST['password']
        R_address = request.POST['address']
        R_phone = request.POST['phone']
        R_mail = request.POST['mail']

        try:
            shop_instance = ShopDetails.objects.get(shopno=R_number)
        except ShopDetails.DoesNotExist:
            context = {'msg': 'Shop number does not exist'}
            return render(request, 'Ration_Shop/Rationshop_officer_register.html', context)

        object_of_RationshopOfficer = RationShopOfficer(
            id_number=R_userid,
            name=R_officername,
            shopno=shop_instance,  
            password=R_password,
            address=R_address,
            phonenumber=R_phone,
            mail=R_mail
        )

        try:
            object_of_RationshopOfficer.save()
        except:
            context = {'msg': 'This Officer Details Already Registered'}
            return render(request, 'Ration_Shop/Rationshop_officer_register.html', context)

        officerdata = RationShopOfficer.objects.all()
        return render(request, 'Ration_Shop/Rationshop_officer_register.html', {'dataofshop': officerdata})

    return render(request, 'Ration_Shop/Rationshop_officer_register.html')

def rationshop_officer_login(request):
    if request.method == 'POST':
        rationshop_officer_name = request.POST.get('officer_name')
        rationshop_officer_password = request.POST.get('officer_password')
        try:
            user=RationShopOfficer.objects.get(name = rationshop_officer_name , password = rationshop_officer_password)
        except RationShopOfficer.DoesNotExist:
            user = None
        if user is not None:
            return redirect('Ration_Shop/Rationshop_billing.html')
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'Ration_Shop/Rationshop_officer_login.html', context)
    return render(request,'Ration_Shop/Rationshop_officer_login.html')

def rationshop_officer_index(request):
    mydata=RationShopStocks.objects.all()
    if(mydata!=''):
        return render(request,'Ration_Shop/Rationshop_index.html',{'datas':mydata})
    else:
        return render(request,'Ration_Shop/Rationshop_index.html')
    
def rationshop_billing(request):
    mydata = CardEntitlement.objects.all()
    
    if request.method == 'POST':
        card_no = request.POST.get('card_number')
        product_name = request.POST.get('product_name')
        quantity = float(request.POST.get('quantity')) # Convert to int
        date = request.POST.get('date')
        try:
            shop_instance = CardDetails.objects.get(card_number=card_no)
            product_instance = ProductPrice.objects.get(product_name=product_name)
            product_name_instance = RationShopStocks.objects.get(productname=product_name)
            price = product_instance.price  # Access price directly
            
            # Check if shop and product exist
            if  product_instance:
                total_cost = quantity * price  # Calculate total cost
                context = {'msg': total_cost}
                
                # Creating a transaction history entry
                  # Save transaction history
                
                # Shop stock updation
                shop_stock = get_object_or_404(RationShopStocks, productname=product_name)
                if quantity <= shop_stock.quantity:
                    shop_stock.quantity -= quantity
                    shop_stock.save()
                else:
                    context = {'msg': 'Insufficient Stock in RationShop'}
                    return render(request, 'Ration_Shop/Rationshop_billing.html', context)
                
                # Card balance quantity updation
                card_balance_quantity = get_object_or_404(CardEntitlement, product_name=product_instance)
                if quantity <= card_balance_quantity.balance_quantity:
                    card_balance_quantity.balance_quantity = card_balance_quantity.balance_quantity - quantity
                    card_balance_quantity.save()
                    object_of_history = Transaction_histroy(
                    card_number=shop_instance,
                    product_name=product_instance,
                    total_cost=total_cost,
                    quantity = quantity,
                    date = date,
                    )
                    object_of_history.save()
                else:
                    context = {'msg': 'Insufficient Stock'}
                    
                    return render(request, 'Ration_Shop/Rationshop_billing.html', context)

                return render(request, 'Ration_Shop/Rationshop_billing.html', context)
            else:
                context = {'msg': 'Details are mismatching'}
                return render(request, 'Ration_Shop/Rationshop_billing.html', context)
        
        except ShopDetails.DoesNotExist or ProductPrice.DoesNotExist:
            context = {'msg': 'Details are mismatching'}
            return render(request, 'Ration_Shop/Rationshop_billing.html', context)
        except RationShopStocks.DoesNotExist:
            context = {'msg': 'This stock not available in this shop'}
            return render(request, 'Ration_Shop/Rationshop_billing.html', context)
    
    return render(request, 'Ration_Shop/Rationshop_billing.html', {'datas': mydata})

def transaction_details(request):
    mydata=Transaction_histroy.objects.all()
    if(mydata!=''):
        return render(request, 'Ration_Shop/transaction_history.html', {'datas': mydata})
    else:
        return render(request, 'Ration_Shop/transaction_history.html')

