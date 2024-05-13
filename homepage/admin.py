from django.contrib import admin
from .models import PasteText, Product

class PasteTextAdmin(admin.ModelAdmin):
    list_display = ('text', 'id')

admin.site.register(PasteText, PasteTextAdmin)
admin.site.register(Product)

# Register your models here.
