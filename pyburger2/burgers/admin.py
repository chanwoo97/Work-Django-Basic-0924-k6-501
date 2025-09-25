from django.contrib import admin

# Register your models here.
from burgers.models import Burger


# Register your models here.
@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    pass