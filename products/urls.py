from . import views
from django.urls import path    

urlpatterns = [
    path('<int:product_id>/', views.product_detail, name = "product_detail" ),
    path('all/', views.all_products, name = "all_products"),
    path('create/', views.add_product, name = "add" ),
    path('edit/<int:product_id>', views.edit_product, name = "edit_product"),
    path('delete/<int:product_id>', views.edit_product, name = "delete"),
   
]