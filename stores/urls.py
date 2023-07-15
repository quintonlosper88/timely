from django.urls import path
from . import views

app_name = 'stores'
print('URLS called')
urlpatterns = [
    path('', views.index, name='index'),
    path('create/',views.ToolCreateView.as_view(),name="toolcreate"),
     path('table/',views.ToolListModelView.as_view(), name='table')
    # More paths related to this app...
]

