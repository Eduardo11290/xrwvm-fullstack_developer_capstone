from django.contrib import admin
from .models import CarMake, CarModel

# Optional: Registering CarModel with a custom ModelAdmin to make it easier to view
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'dealer_id')
    list_filter = ('type', 'car_make', 'year')
    search_fields = ('name', 'car_make__name')

# Registering models with their respective admins
admin.site.register(CarMake)
admin.site.register(CarModel, CarModelAdmin)

