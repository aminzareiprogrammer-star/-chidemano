from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "is_available", "created_at")
    list_filter = ("category", "is_available", "created_at")
    search_fields = ("name", "category", "description")
    list_editable = ("price", "is_available")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)
