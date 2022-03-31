from django.contrib import admin
from .models import ElectricityMeter, Measurement


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'avg_consumption', 'current_value')
    list_display_links = ('name',)


admin.site.register(ElectricityMeter, PersonAdmin)
admin.site.register(Measurement, admin.ModelAdmin)
