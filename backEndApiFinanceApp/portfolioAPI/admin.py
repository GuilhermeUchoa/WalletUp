from django.contrib import admin
from .models import PortfolioModels, AtivosModels


@admin.register(AtivosModels)
class AtivosAdmin(admin.ModelAdmin):

    list_display = [i.name for i in AtivosModels._meta.get_fields()][1:]
    list_editable = ["tipo"]
    list_filter = ["tipo", "atualizacao"]
    search_fields = ["ativo", "tipo"]


@admin.register(PortfolioModels)
class PortfolioAdmin(admin.ModelAdmin):
   
    list_display = ['id', 'usuario', 'ativo', 'cotacao', 'quantidade', 'porcentagem', 'meta', 'dy', 'status', 'tipo', 'aporte', 'precoMedio', 'valuationDy', 'valuationDFC','scoreQualitativo']
    list_filter = ["usuario","tipo","status","ativo"]
    list_editable = ['meta', 'status'] 
    search_fields = ["ativo", "status", "tipo"]
