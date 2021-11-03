from django.contrib import admin
from .models import Income, Debtor, Creditor, SellChicken


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('income_date', 'income_of_small_description',)
    list_filter = ('income_date', 'income_of_small_description',)
    search_fields = ('income_date', 'income_of_small_description',)
    ordering = ['-income_date']


admin.site.register(Income, IncomeAdmin)


class DebtorAdmin(admin.ModelAdmin):
    list_display = ('debtorـdate', 'debtor_of_small_description',)
    list_filter = ('debtorـdate',)
    search_fields = ('debtorـdate', 'debtor_of_small_description',)


admin.site.register(Debtor, DebtorAdmin)


class CreditorAdmin(admin.ModelAdmin):
    list_display = ('creditorـdate', 'creditor_of_small_description',)
    list_filter = ('creditorـdate',)
    search_fields = ('creditorـdate', 'creditor_of_small_description',)


admin.site.register(Creditor, CreditorAdmin)


admin.site.register(SellChicken)
