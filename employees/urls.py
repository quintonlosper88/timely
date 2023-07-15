from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/',views.UserCreateView.as_view(), name='create'),
    path('table/',views.UserModelListView.as_view(), name='table'),
    # More paths related to this app...
]