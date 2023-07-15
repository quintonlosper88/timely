from django.contrib import admin
from employees.models import UserModel
# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'employeeID','job_title', 'email','display_qr_code')

    def display_qr_code(self, obj):
        if obj.qr_code:
            return '<img src="{url}" width="100" height="100" />'.format(url=obj.qr_code.url)
        else:
            return 'No QR Code'

    display_qr_code.short_description = 'QR Code'
    display_qr_code.allow_tags = True

admin.site.register(UserModel, UserModelAdmin)