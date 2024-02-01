from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    antique = Antique.objects.all()
    return render(request,'index.html',{'antique':antique})

def dfadmin(request):
    antique = Antique.objects.all()
    if request.method == 'POST':
        nav1 = request.POST['nav1']
        nav2 = request.POST['nav2']
        nav3 = request.POST['nav3']
        nav4 = request.POST['nav4']

        intro1 = request.POST['intro1']
        intro2 = request.POST['intro2']
        intro3 = request.POST['intro3']
        intro4 = request.POST['intro4']
        intro5 = request.POST['intro5']

        menu_head = request.POST['menu_head']
        menu_img1_1 = request.POST['menu_img1_1']
        menu_img1_2 = request.POST['menu_img1_2']
        menu_img1_3 = request.POST['menu_img1_3']
        menu_img2_1 = request.POST['menu_img2_1']
        menu_img2_2 = request.POST['menu_img2_2']
        menu_img2_3 = request.POST['menu_img2_3']
        menu_img3_1 = request.POST['menu_img3_1']
        menu_img3_2 = request.POST['menu_img3_2']
        menu_img3_3 = request.POST['menu_img3_3']
        menu_img4_1 = request.POST['menu_img4_1']
        menu_img4_2 = request.POST['menu_img4_2']
        menu_img4_3 = request.POST['menu_img4_3']
        menu_img5_1 = request.POST['menu_img5_1']
        menu_img5_2 = request.POST['menu_img5_2']
        menu_img5_3 = request.POST['menu_img5_3']
        menu_img6_1 = request.POST['menu_img6_1']
        menu_img6_2 = request.POST['menu_img6_2']
        menu_img6_3 = request.POST['menu_img6_3']
        menu_img7_1 = request.POST['menu_img7_1']
        menu_img7_2 = request.POST['menu_img7_2']
        menu_img7_3 = request.POST['menu_img7_3']
        menu_img8_1 = request.POST['menu_img8_1']
        menu_img8_2 = request.POST['menu_img8_2']
        menu_img8_3 = request.POST['menu_img8_3']

        about1 = request.POST['about1']
        about2 = request.POST['about2']
        about3 = request.POST['about3']
        about4 = request.POST['about4']

        contact1 = request.POST['contact1']
        contact2 = request.POST['contact2']
        contact3 = request.POST['contact3']
        contact4 = request.POST['contact4']
        contact5 = request.POST['contact5']
        contact6 = request.POST['contact6']
        contact7 = request.POST['contact7']
        contact8 = request.POST['contact8']
        contact9 = request.POST['contact9']

        footer1 = request.POST['footer1']
        footer2 = request.POST['footer2']
        footer3 = request.POST['footer3']
        
    return render(request,'basictable.html',{'antique':antique})