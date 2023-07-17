from django.shortcuts import render
from employees.models import UserModel
from scanner.models import Timesheet
from stores.models import WarehouseModel

# Create your views here.
def index(request):
    employee_count = UserModel.objects.count()
    onsite_employees = Timesheet.objects.filter(leave_time__isnull=True).count()
    tools_count = WarehouseModel.objects.count()
    data = {
        'employee_count':employee_count,
        'onsite_employees':onsite_employees,
        'tools_count':tools_count
    }

    return render(request, 'home/index.html',{'data': data})
