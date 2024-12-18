from django.contrib import admin
from .models import *

admin.site.register(Task)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_dispiay = ('name','price','stock')
    search_fields = ('name','description')
    list_filter = ('price',)
admin.site.register(person)
admin.site.register(employee)
admin.site.register(TimestampedModel)
admin.site.register(Product_1)
admin.site.register(Order)
admin.site.register(DiscountedProduct)
admin.site.register(Product_2)