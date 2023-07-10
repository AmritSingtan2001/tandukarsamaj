from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _



class BannarImage(models.Model):
    image = models.ImageField(upload_to="bannarimage/")

    class Meta:
        ordering = ['-id',]
        


class NoticeBoard(models.Model):
    notic = RichTextField(max_length="100")
    created_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-id',]
    
    def  __str__(self):
        return self.notic


class News(models.Model):
    title = models.CharField(max_length=350)
    image  = models.ImageField(upload_to='newsimage/')
    discriptions = RichTextField()
    created_date = models.DateField(auto_now=True)
    news_slug = AutoSlugField(populate_from ='title', unique=True, default=None)

    
    class Meta:
        ordering =['-id',]
    
    def __str__(self):
        return self.title



class Press(models.Model):
    title = models.CharField(max_length = 250)
    image = models.ImageField(upload_to='pressimage/')
    discriptions = RichTextField()
    create_date = models.DateField(auto_now=True)
    press_slug = AutoSlugField(populate_from ='title', unique=True, default=None)

    class Meta:
        ordering =['-id',]

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length = 250)
    image = models.ImageField(upload_to='eventimage/')
    discriptions = RichTextField()
    event_slug = AutoSlugField(populate_from ='title', unique=True, default=None)

    class Meta:
        ordering =['-id',]

    def __str__(self):
        return self.title
    


class Gallery(models.Model):
    title = models.CharField(max_length=250)
    img_slug = AutoSlugField(populate_from ='title', unique=True, null=True, default=None)

    class Meta:
        ordering =['-id',]
    
    def __str__(self):
        return self.title
    

class Image(models.Model):
    title = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='galleryimage/')

    class Meta:
        ordering = ['id',]
    



class Video(models.Model):
    video_url = models.URLField()
    discriptions=RichTextField(null=True, blank=True)

    class Meta:
        ordering =['-id',]


class ExecutiveMember(models.Model):
    full_name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    phone_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='executiveimage/')

    class Meta:
        ordering = ['id',]

    def __str__(self):
        return self.full_name


class About(models.Model):
    title = models.CharField(max_length=150)
    about_slug = AutoSlugField(populate_from ='title', unique=True, default=None)

    def __str__(self):
        return self.title
    
class AboutUs(models.Model):
    category = models.ForeignKey(About, on_delete=models.CASCADE, related_name='category')
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='aboutimage/', null=True, blank=True)
    discription = RichTextField()
 
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title









class OrdinaryMember(models.Model):

    choose = (
        ('verify','Verify'),
        ('not_verify','Not Verfiry')
    )

    member = (
        ('life time','Life Time'),
        ('ordinary','Ordinary')
    )

    fullname = models.CharField(max_length=150)
    phone_number = models.PositiveIntegerField()
    email = models.EmailField()
    image = models.ImageField(upload_to='ordinarymemberimage/')
    grand_father_name = models.CharField(max_length=150)
    father_name = models.CharField(max_length=150)
    mother_name = models.CharField(max_length=150)
    son_name = models.CharField(max_length=150, null=True, blank=True)
    daughter_name = models.CharField(max_length=150,null=True, blank=True)
    temporary_address = models.CharField(max_length=150)
    permanent_address = models.CharField(max_length=150)
    country = models.CharField(max_length=150, null=True, blank=True)
    qualification = models.CharField(max_length=150, null=True, blank=True)
    documents = models.FileField(upload_to='documents/')
    membertype= models.CharField(choices=member, max_length=50)
    status = models.CharField(choices=choose, default='not_verify', max_length=50)
   
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.fullname
    



class ContactInfo(models.Model):
    phone_number = models.PositiveIntegerField()
    address = models.CharField(max_length=150)
    email = models.EmailField()
    facebook_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    instagram_url  = models.URLField(null=True, blank=True)
    tiktok_url = models.URLField(null=True, blank=True)


    class Meta:
        ordering =['-id',]



class BankDetails(models.Model):
    bank_name = models.CharField(max_length=150)
    account_number = models.PositiveIntegerField()
    branch_name = models.CharField(max_length=150)
    qr_code  = models.ImageField(upload_to='qrcode/')

    class Meta:
        ordering = ['-id',]

    def __str__(self):
        return self.bank_name


class Manifesto(models.Model):
    image = models.ImageField(upload_to="Manifesto/")

    class Meta:
        ordering = ['id']

    

class Keyword(models.Model):
    website_keyword=models.TextField()

    class Meta:
        ordering =['-id']

    
class Discription(models.Model):
    website_discription = models.TextField()

    class Meta:
        ordering = ['-id']

class Auth(models.Model):
    website_auth = models.CharField(max_length=200)
     
    class Meta:
        ordering = ['-id',]



class NoticImage(models.Model):
    image= models.ImageField(upload_to='noticeimage/')


    class Meta:
        ordering = ['-id',]



class Branch(models.Model):
    branch_name_nepali= models.CharField(max_length=150)
    branch_name_english= models.CharField(max_length=150)

    class Meta:
        ordering = ['-id',]

    def __str__(self):
        return self.branch_name_english