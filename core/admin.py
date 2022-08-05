from django.contrib import admin

from .models import CapitaisEstados

@admin.register(CapitaisEstados)
class RegistraModelos(admin.ModelAdmin):
    list_display = [
        'estado', 'capital', 'habitantes'
    ]
