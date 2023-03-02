from django.urls import path
from . import views

urlpatterns = [
  #Login
  path('',views.login, name='login'),
  #Sign Up
  path('sign_up',views.sign_up, name='sign_up'),
  #Home
  path('home',views.home, name='home'),
  #Change Password
  path('change_password',views.change_password, name='change_password'),
  #Product List
  path('product_list',views.product_list, name='product_list'),
  #Add Product
  path('add_product', views.add_product, name="add_product"),
  #Update Product
  path('update_product/<str:productID>',views.update_product, name="update_product"),
  path('update_product/save_update_product/<str:productID>',views.save_update_product, name="save_update_product"),
  #Delete
  path('delete_product/<str:productID>',views.delete_product, name="delete_product"),
  #Stock In/Out
  path('stock_in_out', views.stock_in_out, name='stock_in_out'),
  #Stock In/Out History
  path('stock_in_out_history', views.stock_in_out_history, name='stock_in_out_history'),
  #Asked Question
  path('asked_question',views.asked_question, name='asked_question'),
  #Add Question
  path('add_question',views.add_question, name='add_question'),
  #My Question
  path('my_pending_question',views.my_pending_question, name='my_pending_question'),
  #Delete My Question
  path('delete_my_question',views.delete_my_question, name="delete_my_question"),
]