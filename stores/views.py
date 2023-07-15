from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView,UpdateView
from django.urls import reverse_lazy
from .models import WarehouseModel
from .forms import ToolForm
# Create your views here.
def index(request):
    return render(request, 'stores/index.html')

class ToolListModelView(ListView):
    model = WarehouseModel
    template_name = 'stores/table.html'
    context_object_name = 'toolmodels'

class ToolCreateView(CreateView):
    print("ToolCreatEView Called")
    model = WarehouseModel
    form_class = ToolForm
    template_name = 'stores/create.html'
    success_url = reverse_lazy('stores:table')

    def form_valid(self, form):
        print("form valid function called")
        # Save the form instance and get the created object
        self.object = form.save()

        # You can perform additional actions here if needed

        return super().form_valid(form)