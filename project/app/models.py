from django.db import models

# Create your models here.

class Antique(models.Model):
    # navbar
    main_img = models.ImageField(upload_to='gallery')
    nav1 = models.CharField(max_length=100)
    nav2 = models.CharField(max_length=100)
    nav3 = models.CharField(max_length=100)
    nav4 = models.CharField(max_length=100)

    #intro
    intro1 = models.CharField(max_length=100)
    intro2 = models.CharField(max_length=100)
    intro3 = models.TextField()
    intro4 = models.TextField()
    intro5 = models.TextField()

    #menu_main
    menu_mainimg = models.ImageField(upload_to='gallery')
    menu_head = models.CharField(max_length=100)

    menu_img1 = models.ImageField(upload_to="gallery")
    menu_img1_1 = models.CharField(max_length=100)
    menu_img1_2 = models.CharField(max_length=100)
    menu_img1_3 = models.CharField(max_length=100)

    menu_img2 = models.ImageField(upload_to="gallery")
    menu_img2_1 = models.CharField(max_length=100)
    menu_img2_2 = models.CharField(max_length=100)
    menu_img2_3 = models.CharField(max_length=100)

    menu_img3 = models.ImageField(upload_to="gallery")
    menu_img3_1 = models.CharField(max_length=100)
    menu_img3_2 = models.CharField(max_length=100)
    menu_img3_3 = models.CharField(max_length=100)

    menu_img4 = models.ImageField(upload_to="gallery")
    menu_img4_1 = models.CharField(max_length=100)
    menu_img4_2 = models.CharField(max_length=100)
    menu_img4_3 = models.TextField()

    menu_img5 = models.ImageField(upload_to="gallery")
    menu_img5_1 = models.CharField(max_length=100)
    menu_img5_2 = models.CharField(max_length=100)
    menu_img5_3 = models.CharField(max_length=100)

    menu_img6 = models.ImageField(upload_to="gallery")
    menu_img6_1 = models.CharField(max_length=100)
    menu_img6_2 = models.CharField(max_length=100)
    menu_img6_3 = models.CharField(max_length=100)

    menu_img7 = models.ImageField(upload_to="gallery")
    menu_img7_1 = models.CharField(max_length=100)
    menu_img7_2 = models.CharField(max_length=100)
    menu_img7_3 = models.CharField(max_length=100)

    menu_img8 = models.ImageField(upload_to="gallery")
    menu_img8_1 = models.CharField(max_length=100)
    menu_img8_2 = models.CharField(max_length=100)
    menu_img8_3 = models.CharField(max_length=100)

    # about
    about_img = models.ImageField(upload_to="gallery")
    about1 = models.CharField(max_length=100)
    about2 = models.TextField()
    about3 = models.TextField()
    about4 = models.CharField(max_length=100)

    #contact
    contact_img = models.ImageField(upload_to='gallery')
    contact1 = models.CharField(max_length=100)
    contact2 = models.TextField()
    contact3 = models.TextField()
    contact4 = models.TextField()
    contact5 = models.TextField()
    contact6 = models.TextField()
    contact7 = models.TextField()
    contact8 = models.TextField()
    contact9 = models.TextField()

    # footer
    footer1 = models.CharField(max_length=100)
    footer2 = models.CharField(max_length=100)
    footer3 = models.CharField(max_length=100)