from . import views
from django.urls import path    

urlpatterns = [
    path('', views.product_detail, name = "home" ),
    path('create/', views.add_product, name = "add" ),
    path('edit/<int:product_id>', views.edit_product, name = "edit_product"),
   
]