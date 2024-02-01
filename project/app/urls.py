from django.urls import path
from . import views

app_name = 'antique'
urlpatterns = [
    path('',views.home,name='home'),
    path('admin/',views.admin,name='admin'),
]