from django.contrib import admin
from .models import Daily_Informations, DrugRegistration, VaccineRegistration, WeightRegistration

# Register your models here.

admin.site.site_header = "سامانه مدیریت فارم"


class Daily_InformationsAdmin(admin.ModelAdmin):
    list_display = ('hall', 'date', 'hall', 'losses', 'knockout', 'temprature_max',
                    'temprature_min', 'seed', 'price',)
    list_filter = ('hall', 'date',)
    search_fields = ('date', 'hall', 'losses', 'knockout', 'temprature_max',
                     'temprature_min', 'seed', 'price',)
    ordering = ['-date']


admin.site.register(Daily_Informations, Daily_InformationsAdmin)


class DrugRegistrationAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id',)
    search_fields = ('id',)
    ordering = ['-id']


admin.site.register(DrugRegistration, DrugRegistrationAdmin)


class VaccineRegistrationAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id',)
    search_fields = ('id',)
    ordering = ['-id']


admin.site.register(VaccineRegistration, VaccineRegistrationAdmin)


class WeightRegistrationAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id',)
    search_fields = ('id',)
    ordering = ['-id']


admin.site.register(WeightRegistration, WeightRegistrationAdmin)
