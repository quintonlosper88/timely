from django.urls import path
from . import views

app_name = 'scanner'

urlpatterns = [
    path('', views.index, name='index'),
    path('security/',views.securityView,name='security'),
    path("user/",views.userscannedView,name="userscanned"),
    path('timesheets/',views.TimesheetModelListView.as_view(),name="timesheets")
    # More paths related to this app...
]