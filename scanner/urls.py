from django.urls import path
from . import views

app_name = 'scanner'

urlpatterns = [
    path('', views.index, name='index'),
    path('security/',views.securityView,name='security'),
    path("user/",views.userscannedView,name="userscanned")
    # More paths related to this app...
]