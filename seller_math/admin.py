from django.contrib import admin

from seller_math.models import CsvSeller


@admin.register(CsvSeller)
class CsvSellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'summe', 'zip',)
    search_fields = list_display
