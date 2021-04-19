from django.contrib import admin
from .models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('title', 'discounted_price', 'model')

admin.site.register(Car, CarAdmin)

# Register your models here.
