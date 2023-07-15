from django.contrib import admin
from scanner.models import Timesheet,ToolCheckoutModel
# Register your models here.

class TimesheetModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'enter_time', 'leave_time']
    list_filter = ['user', 'enter_time']
    search_fields = ['user__employeeID', 'user__firstName', 'user__lastName']

admin.site.register(Timesheet, TimesheetModelAdmin)

class ToolCheckOutModelAdmin(admin.ModelAdmin):
    list_display = ['tool', 'checkout_date', 'employee','return_date','condition_rating']
    list_filter = ['tool', 'checkout_date']


admin.site.register(ToolCheckoutModel, ToolCheckOutModelAdmin)