from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def home(request):
    antique = Antique.objects.all()
    return render(request,'index.html',{'antique':antique})

def admin(request):
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

        Antique.objects.all().update(nav1=nav1,nav2=nav2,nav3=nav3,nav4=nav4,intro1=intro1,intro2=intro2,intro3=intro3,intro4=intro4,intro5=intro5,
                                     menu_head=menu_head,menu_img1_1=menu_img1_1,menu_img1_2=menu_img1_2,menu_img1_3=menu_img1_3,
                                     menu_img2_1=menu_img2_1,menu_img2_2=menu_img2_2,menu_img2_3=menu_img2_3,menu_img3_1=menu_img3_1,menu_img3_2=menu_img3_2,menu_img3_3=menu_img3_3,
                                     menu_img4_1=menu_img4_1,menu_img4_2=menu_img4_2,menu_img4_3=menu_img4_3,menu_img5_1=menu_img5_1,menu_img5_2=menu_img5_2,menu_img5_3=menu_img5_3,
                                     menu_img6_1=menu_img6_1,menu_img6_2=menu_img6_2,menu_img6_3=menu_img6_3,menu_img7_1=menu_img7_1,menu_img7_2=menu_img7_2,menu_img7_3=menu_img7_3,
                                     menu_img8_1=menu_img8_1,menu_img8_2=menu_img8_2,menu_img8_3=menu_img8_3,contact1=contact1,contact2=contact2,contact3=contact3,contact4=contact4,
                                     contact5=contact5,contact6=contact6,contact7=contact7,contact8=contact8,contact9=contact9,
                                     footer1=footer1,footer2=footer2,footer3=footer3)
        
    return render(request,'basictable.html',{'antique':antique})

def mainimg(request):
    if request.method == 'POST':
        about_img = request.FILES.get('main_img')
        antique_instance = Antique.objects.first()  # You may want to retrieve the specific instance you want to update
        antique_instance.about_img = about_img
        antique_instance.save()
        return redirect('app:admin')

def menumainimg(request):
    if request.method == 'POST':
        about_img = request.FILES.get('menu_mainimg')
        antique_instance = Antique.objects.first()  # You may want to retrieve the specific instance you want to update
        antique_instance.about_img = about_img
        antique_instance.save()
        return redirect('app:admin')
    
def menuimg1(request):
    if request.method == 'POST':
        about_img = request.FILES.get('menu_img1')
        antique_instance = Antique.objects.first()  # You may want to retrieve the specific instance you want to update
        antique_instance.about_img = about_img
        antique_instance.save()
        return redirect('app:admin')
    
def menuimg2(request):
    if request.method == 'POST':
        about_img = request.FILES.get('menu_img2')
        antique_instance = Antique.objects.first()  # You may want to retrieve the specific instance you want to update
        antique_instance.about_img = about_img
        antique_instance.save()
        return redirect('app:admin')
    
def menuimg3(request):
    if request.method == 'POST':
        about_img = request.FILES.get('menu_img3')
        antique_instance = Antique.objects.first()  # You may want to retrieve the specific instance you want to update
        antique_instance.about_img = about_img
        antique_instance.save()
        return redirect('app:admin')
    
def menuimg4(request):
    if request.method == 'POST':
        about_img = request.FILES.get('menu_img4')
        antique_instance = Antique.objects.first()  # You may want to retrieve the specific instance you want to update
        antique_instance.about_img = about_img
        antique_instance.save()
        return redirect('app:admin')
    
def menuimg5(request):
    if request.method == 'POST':
        about_img = request.FILES.get('menu_img5')
        antique_instance = Antique.objects.first()  # You may want to retrieve the specific instance you want to update
        antique_instance.about_img = about_img
        antique_instance.save()
        return redirect('app:admin')
    
def menuimg6(request):
    if request.method == 'POST':
        about_img = request.FILES.get('menu_img6')
        antique_instance = Antique.objects.first()  # You may want to retrieve the specific instance you want to update
        antique_instance.about_img = about_img
        antique_instance.save()
        return redirect('app:admin')
    
def menuimg7(request):
    if request.method == 'POST':
        about_img = request.FILES.get('menu_img7')
        antique_instance = Antique.objects.first()  # You may want to retrieve the specific instance you want to update
        antique_instance.about_img = about_img
        antique_instance.save()
        return redirect('app:admin')
    
def menuimg8(request):
    if request.method == 'POST':
        about_img = request.FILES.get('menu_img8')
        antique_instance = Antique.objects.first()  # You may want to retrieve the specific instance you want to update
        antique_instance.about_img = about_img
        antique_instance.save()
        return redirect('app:admin')
    
def aboutimg(request):
    if request.method == 'POST':
        about_img = request.FILES.get('abou_img')
        antique_instance = Antique.objects.first()  # You may want to retrieve the specific instance you want to update
        antique_instance.about_img = about_img
        antique_instance.save()
        return redirect('app:admin')
    
def contactimg(request):
    if request.method == 'POST':
        about_img = request.FILES.get('contact_img')
        antique_instance = Antique.objects.first()  # You may want to retrieve the specific instance you want to update
        antique_instance.about_img = about_img
        antique_instance.save()
        return redirect('app:admin')