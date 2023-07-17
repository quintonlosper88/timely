from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserModel,Timesheet
from django.utils import timezone
from datetime import datetime
from django.views.generic import ListView,UpdateView
from django.http import HttpResponse
import csv
# Create your views here.
def index(request):
    return render(request, 'scanner/index.html')

def securityView(request):
    return render(request, 'scanner/security.html')

@csrf_exempt
def userscannedView(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        employee_id = data.get('employeeId')
        status = data.get('status')
        timestamp = data.get('timestamp')
        print("timestamp variable {} of type {}".format(timestamp,type(timestamp)))


        # Retrieve user details from the database
        try:
            user = UserModel.objects.get(employeeID=employee_id)
            user_data = {
                "firstName": user.firstName,
                "lastName": user.lastName,
                "email": user.email,
                "employeeID": user.employeeID,
                'profileImage': user.profileImage.url if user.profileImage else None,
                # Include other user details as needed
            }
        except UserModel.DoesNotExist:
            # Handle case when user does not exist
            return JsonResponse({"message": "User not found"})

        scanned_datestamp=datetime.strptime(timestamp,"%Y-%m-%d %H:%M:%S").date()
        print("scanned datestamp that is converted to date {} of type {}".format(scanned_datestamp,type(scanned_datestamp)))
        # Get the current date
        current_datetime = timezone.now()
        # Check if there is an existing entry for the user and the same date
        existing_entry = Timesheet.objects.filter(user=user, enter_time__date=current_datetime.date()).first()

        if existing_entry:
            if status == 'Enter':
                # Check if an existing entry with 'Enter' status already exists for today
                return JsonResponse({"message": "Timesheet entry already exists for today"})
            elif status == 'Leave':
                # Check if an existing entry with 'Leave' status already exists for today
                if existing_entry.leave_time:
                    return JsonResponse({"message": "User already signed out"})
                else:
                    # Update the existing entry with the leave time
                    existing_entry.leave_time = current_datetime
                    existing_entry.duration = current_datetime - existing_entry.enter_time
                    existing_entry.save()
        else:
            # Create a new timesheet entry
            if status == 'Enter':
                Timesheet.objects.create(user=user, enter_time=current_datetime)
            elif status == 'Leave':
                return JsonResponse({"message": "No active timesheet entry found"})

        # Prepare the response data
        response_data = {
            "message": "Data received and processed successfully",
            "employeeId": employee_id,
            "status": status,
            "timestamp": timestamp,
            "user": user_data
        }

        return JsonResponse(response_data)
    else:
        return JsonResponse({"message": "Invalid request method"})

class TimesheetModelListView(ListView):
    model = Timesheet
    template_name = 'scanner/timesheettable.html'
    context_object_name = 'time_model'

def export_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="timedata.csv"'

    # Fetch data from the database (replace YourModel with your actual model)
    data = Timesheet.objects.all()

    # Create a CSV writer and write the data to the response
    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Employee ID', "Date","Start Time","End Time","Duration"])  # Add field names as column headers

    for item in data:
        # Replace 'field1', 'field2', 'field3', ... with actual field names of your model
        writer.writerow([item.user.firstName, item.user.lastName, item.user.employeeID,item.enter_date,item.enter_time,item.leave_time,item.duration ])

    return response