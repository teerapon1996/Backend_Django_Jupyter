from django.contrib import admin
from ecommerce.models import *

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Location._meta.fields]
@admin.register(Move)
class MoveAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Move._meta.fields]
@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Seller._meta.fields]
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ProductCategory._meta.fields]
@admin.register(ProductSubCategory)
class ProductSubCategoryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ProductSubCategory._meta.fields]
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Product._meta.fields]
@admin.register(Inbound)
class InboundAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Inbound._meta.fields]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Profile._meta.fields]

@admin.register(SaleOrder)
class SaleOrderAdmin(admin.ModelAdmin):
    list_display = [f.name for f in SaleOrder._meta.fields]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [f.name for f in OrderItem._meta.fields]

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Payment._meta.fields]

@admin.register(PackItem)
class PackItemAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PackItem._meta.fields]

@admin.register(PickItem)
class PickItemtemAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PickItem._meta.fields]

@admin.register(PackRequest)
class PackRequestAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PackRequest._meta.fields]
@admin.register(PickRequest)
class PickRequestAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PickRequest._meta.fields]
    
@admin.register(DeliveryStatusTracking)
class DeliveryStatusTrackingAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DeliveryStatusTracking._meta.fields]

