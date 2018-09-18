from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productlisting', views.productlists),
    path('detail/<int:product_id>', views.productdetail, name="productdetail"),
    path('orderlisting', views.orderlists),
    path('orderdetail/<int:order_id>', views.orderdetail, name="orderdetail")
]
