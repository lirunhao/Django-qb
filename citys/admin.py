from django.contrib import admin

# Register your models here.
from citys.models import CitysModel


class CityModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_popular', 's_letter')
    fields = ('name', 'is_popular', 's_letter')


admin.site.register(CitysModel, CityModelAdmin)
