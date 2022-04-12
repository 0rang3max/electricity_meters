from django.contrib import admin
from .models import ElectricityMeter, Measurement


class MeasurementInline(admin.TabularInline):
    model=Measurement
    ordering=('date',)


class ElectricityMeterAdmin(admin.ModelAdmin):
    ordering=('date_start',)
    list_display = ('name', 'avg_consumption', 'current_value')
    list_display_links = ('name',)
    inlines = [
        MeasurementInline,
    ]

class MeasurementAdmin(admin.ModelAdmin):
    ordering=('date',)
    list_display = ('date', 'electricity_meter', 'value',)
    list_filter = ('electricity_meter', 'date')


admin.site.register(ElectricityMeter, ElectricityMeterAdmin)
admin.site.register(Measurement, MeasurementAdmin)
