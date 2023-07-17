from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/',views.UserCreateView.as_view(), name='create'),
    path('table/',views.UserModelListView.as_view(), name='table'),
    path('edit/<int:pk>/',views.UserModelUpdateView.as_view(), name='edit'),
    path('filtered-data/', views.CustomFilteredListView.as_view(), name='filtered_data'),
    path('filternames/', views.employeeFilterView, name='filternames'),

    # More paths related to this app...
]