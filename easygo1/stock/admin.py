from django.contrib import admin
from .models import Staff, Product, StocksManagement, AskQuestion

# Register your models here.
admin.site.register(Staff)
admin.site.register(Product)
admin.site.register(StocksManagement)
admin.site.register(AskQuestion)