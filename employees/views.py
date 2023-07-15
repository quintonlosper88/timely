
from django.views import View
from django.shortcuts import render, redirect
from .models import UserModel
from .forms import UserForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
def index(request):
    return render(request, 'employees/index.html')

# def userTableView(request):
#     template = 'employees/table.html'
#     contx = {}
#     return render(request, template, contx)

class UserModelListView(ListView):
    model = UserModel
    template_name = 'employees/table.html'
    context_object_name = 'usermodels'

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