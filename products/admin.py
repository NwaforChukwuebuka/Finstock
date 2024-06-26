from django.contrib import admin
from .models import Product, Category, ProductImage, Review

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('image', 'alt_text')

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    fields = ('user', 'rating', 'comment', 'created_at')
    readonly_fields = ('created_at',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'created', 'modified')  # Adjusted to use 'created' and 'modified'
    list_filter = ('category', 'created', 'modified')  # Adjusted to use 'created' and 'modified'
    search_fields = ('name', 'description', 'sku')
    inlines = [ProductImageInline, ReviewInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'alt_text')
    search_fields = ('product__name',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'comment', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('product__name', 'user__username', 'comment')
    readonly_fields = ('created_at',)
