from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'descricao', 'disponivel')
    search_fields = ('nome', 'valor', 'descricao', 'disponivel')
    list_per_page = 10
    ordering = ('nome',)