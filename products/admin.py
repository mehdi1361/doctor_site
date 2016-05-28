from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from .models import Category, Product, ProductImages
# Register your models here.
class CategoryFilter(SimpleListFilter):
    title = 'category'
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(parent__isnull=True).values_list('id', 'title')

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(parent__isnull=True)
        else:
            return queryset


class ProductImageAdmin(admin.TabularInline):
    model = ProductImages


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "parent", "category_type", "create_time", "title", "slug", "avatar", "is_enable"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('title', 'slug', )
    list_filter = (CategoryFilter, "is_enable",)
    list_editable = ("parent", "is_enable", )
    list_display = ["id", "title", "create_time", "slug", "get_categories", "parent", "avatar", "is_enable"]
    inlines = [ProductImageAdmin]

    def get_categories(self, obj):
        return " _ ".join([c.title for c in obj.category.all()])
