from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^home/$', views.home, name='home'),
    url(r'^addprice/$',views.addprice, name='addprice'),
    url(r'^pricelist/$',views.pricelist, name='pricelist'),
    url(r'^shopregister/$',views.shopregister, name='shopregister'),
    url(r'^stocks/$',views.shopstock, name='stocks'),
    url(r'^addshopstock/$',views.addshopstock, name='addshopstock'),
    url(r'^stocklist/$',views.shoplist, name='shoplist'),
    url(r'^entitle_list/$',views.entitle_list, name='entitle_list'),
    path('update_price/<str:product_name>/', views.update_price, name='update_price'),
    path('update_stock/<int:id>/',views.update_stock, name='update_stock'),
    path('entitlement_update/<int:id>/',views.update_remaining_stock, name='entitlement_update'),
    url(r'^collector/$', views.collector_login, name='collector_login'),
    url(r'^collector_register/$', views.collector_register, name='collector_register'),
    url(r'^collector_index/$', views.collector_index, name='collector_index'),
    url(r'^collector_shoplist/$', views.collector_shoplist, name='collector_shoplist'),
    url(r'^collector_stocklist/$', views.collector_stocklist, name='collector_stocklist'),
    url(r'^collector_pricelist/$', views.collector_pricelist, name='collector_pricelist'),
    url(r'^rationshop_officer_register/$', views.rationshop_officer_register, name='rationshop_officer_register'),
    url(r'^rationshop/$', views.rationshop_officer_login, name='rationshop'),
    url(r'^rationshop_index/$', views.rationshop_officer_index, name='rationshop_index'),
    url(r'^e_card/$', views.rationcard_details, name='e_card'),
    url(r'^card_entitlement/$', views.entitlement, name='card_entitlement'),
    url(r'^rationshop_billing_index/$', views.rationshop_billing, name='rationshop_billing_index'),
    url(r'^transaction_details/$', views.transaction_details, name='transaction_details'),
    #url(r'^display_details/$', views.display_details, name='display_details'),

 ]