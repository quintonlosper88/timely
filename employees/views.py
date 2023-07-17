
from django.views import View
from django.shortcuts import render, redirect
from .models import UserModel
from .forms import UserForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView,UpdateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'employees/index.html')

class UserModelListView(ListView):
    model = UserModel
    template_name = 'employees/table.html'
    context_object_name = 'usermodels'

class UserModelUpdateView(UpdateView):
    print("user update class based model called")
    model = UserModel
    template_name = 'employees/edit.html'
    form_class = UserForm
    success_url = reverse_lazy('employees:table')


    def form_valid(self, form):
        print("form_valid function called")
        # Save the form instance and get the updated object
        self.object = form.save()

        # Perform any additional actions or logic here

        return super().form_valid(form)


class UserCreateView(CreateView):
    print("UserCreatEView Called")
    model = UserModel
    form_class = UserForm
    template_name = 'employees/create.html'
    success_url = reverse_lazy('employees:table')

    def form_valid(self, form):
        print("form valid function called")
        # Save the form instance and get the created object
        self.object = form.save()

        # You can perform additional actions here if needed

        return super().form_valid(form)

class CustomFilteredListView(ListView):
    print("customerfilterclassed called")
    model = UserModel

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_value = self.request.GET.get('filter_param')

        if filter_value:
            queryset = queryset.filter(some_field=filter_value)
            print(queryset)

        return queryset

    def get(self, request, *args, **kwargs):
        # Check if the request is an AJAX request
        if request.is_ajax():
            queryset = self.get_queryset()
            print('AJAX Queryset ' + queryset)
            # Convert the filtered queryset to a list of dictionaries
            data = list(queryset.values())

            # Return the filtered data as JSON response
            return JsonResponse(data, safe=False)

        # For non-AJAX requests, fall back to the default behavior of the view
        return super().get(request, *args, **kwargs)
@csrf_exempt
def employeeFilterView(request):
    if request.method == 'POST':
        data = request.POST.get('input_data')
        filtered_users = UserModel.objects.filter(firstName__startswith=data)

        # Accessing the firstName field for each object in the queryset
        firstName = [user.firstName for user in filtered_users]
        lastName = [user.lastName for user in filtered_users]
        email = [user.email for user in filtered_users]
        employeeID = [user.employeeID for user in filtered_users]
        date_joined = [user.date_joined for user in filtered_users]
        job_title = [user.job_title for user in filtered_users]

        # Return the filtered data as JSON response
        response_data = {'firstName': firstName,
                         'lastName':lastName,
                         'email':email,
                         'employeeID':employeeID,
                         'date_joined':date_joined,
                         'job_title':job_title
                         }
        return JsonResponse(response_data)
    else:
        # Handle other HTTP methods (GET, PUT, DELETE) if needed
        return JsonResponse({'error': 'Invalid method'})

