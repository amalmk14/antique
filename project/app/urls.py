from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('',views.home,name='home'),
    path('admin/',views.admin,name='admin'),
    path('mainimg/',views.mainimg,name='mainimg'),
    path('menumainimg/',views.menumainimg,name='menumainimg'),
    path('menuimg1/',views.menuimg1,name='menuimg1'),
    path('menuimg2/',views.menuimg2,name='menuimg2'),
    path('menuimg3/',views.menuimg3,name='menuimg3'),
    path('menuimg4/',views.menuimg4,name='menuimg4'),
    path('menuimg5/',views.menuimg5,name='menuimg5'),
    path('menuimg6/',views.menuimg6,name='menuimg6'),
    path('menuimg7/',views.menuimg7,name='menuimg7'),
    path('menuimg8/',views.menuimg8,name='menuimg8'),
    path('aboutimg/',views.aboutimg,name='aboutimg'),
    path('contactimg/',views.contactimg,name='contactimg'),
]