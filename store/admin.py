from django.contrib import admin
from store.models import Category,Product,Size,OrderItems,Order,Tag


# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(OrderItems)
admin.site.register(Order)
admin.site.register(Tag)
