from django.contrib import admin
from .models import PortfolioModels, AtivosModels


@admin.register(AtivosModels)
class AtivosAdmin(admin.ModelAdmin):

    
    list_display = ['ativoPrincipal', 'cotacao', 'tipo', 'dy', 'pl', 'enterpriseValue', 'freeCashflow', 'revenueGrowth', 'debtToEquity', 'earningsQuarterlyGrowth', 'twoHundredDayAverage', 'fiftyTwoWeekLow', 'fiftyTwoWeekHigh', 'atualizacao']
    list_editable = ["tipo"]
    list_filter = ["tipo", "atualizacao"]
    search_fields = ["ativo", "tipo"]


@admin.register(PortfolioModels)
class PortfolioAdmin(admin.ModelAdmin):
   
    list_display = ['id', 'usuario', 'ativo', 'cotacao', 'quantidade', 'dy','porcentagem', 'meta', 'status', 'tipo', 'aporte', 'precoMedio', 'valuationDy', 'valuationDFC','scoreQualitativo']
    list_filter = ["usuario","tipo","status","ativo"]
    list_editable = ['meta', 'status'] 
    search_fields = ["ativo", "status", "tipo"]
