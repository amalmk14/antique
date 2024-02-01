from django.urls import path
from . import views

app_name = 'antique'
urlpatterns = [
    path('',views.home,name='home'),
    path('dfadmin/',views.dfadmin,name='dfadmin'),
]