from django.urls import path
from . import views

app_name = 'scanner'

urlpatterns = [
    path('', views.index, name='index'),
    path('security/',views.securityView,name='security'),
    path("user/",views.userscannedView,name="userscanned"),
    path('timesheets/',views.TimesheetModelListView.as_view(),name="timesheets"),
    path('export/', views.export_to_csv, name='export_to_csv'),
    path('report/', views.report, name="report")
    # More paths related to this app...
]