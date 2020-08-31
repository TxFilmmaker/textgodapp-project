from django.contrib import admin

# Register your models here.
from .models import TKjv

class TKjvAdmin(admin.ModelAdmin):
    list_display = ("id", "b", "c", "v", "book")

admin.site.register(TKjv, TKjvAdmin)
