from django.contrib import admin
from .models import Cost, Income, Debtor, Creditor, SellChicken


class CostAdmin(admin.ModelAdmin):
    list_display = ('cost_title', 'cost_type', 'cost_amount', 'cost_date',)
    list_filter = ('cost_type', 'cost_date',)
    search_fields = ('cost_title', 'cost_type', 'cost_amount', 'cost_revenue', 'cost_date',)
    ordering = ['-cost_date']


admin.site.register(Cost, CostAdmin)


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('income_date', 'income_the_amount',)
    list_filter = ('income_date', 'income_the_amount',)
    search_fields = ('income_date', 'income_the_amount',)
    ordering = ['-income_date']


admin.site.register(Income, IncomeAdmin)


class DebtorAdmin(admin.ModelAdmin):
    list_display = ('debtor_of_small_description', 'debtor_the_amount',)
    list_filter = ('debtor_the_amount',)
    search_fields = ('debtor_of_small_description', 'debtor_the_amount',)


admin.site.register(Debtor, DebtorAdmin)


class CreditorAdmin(admin.ModelAdmin):
    list_display = ('creditor_of_small_description', 'creditor_the_amount',)
    list_filter = ('creditor_the_amount',)
    search_fields = ('creditor_of_small_description', 'creditor_the_amount',)


admin.site.register(Creditor, CreditorAdmin)


admin.site.register(SellChicken)
