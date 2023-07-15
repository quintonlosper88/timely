from django.contrib import admin
from stores.models import WarehouseModel
# Register your models here.
class WarehouseModelAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'manufacturer', 'serial_number', 'display_qr_code')

    def display_qr_code(self, obj):
        if obj.qr_code:
            return '<img src="{url}" width="100" height="100" />'.format(url=obj.qr_code.url)
        else:
            return 'No QR Code'

    display_qr_code.short_description = 'QR Code'
    display_qr_code.allow_tags = True

admin.site.register(WarehouseModel, WarehouseModelAdmin)