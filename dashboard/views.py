from django.shortcuts import render,HttpResponse, HttpResponseRedirect,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . decorators import login_required
from django.contrib import messages
from django.contrib import auth
from . new_file_handler import validate_file
from app.models import News, Event,Press,ExecutiveMember,OrdinaryMember,About,AboutUs,\
    Manifesto,ContactInfo,BankDetails,Image,Gallery,BannarImage,NoticeBoard,Video,Branch

def login(request):
    try:
        if request.user.is_authenticated:
            return render(request,'dashboard/index.html')

        if request.method =="POST":
            username = request.POST['username']
            password = request.POST['password']
            user_obj = User.objects.filter(username= username)
            if not user_obj.exists():
                messages.error(request,"Invalid username...")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                
            
            user_obj = authenticate(username=username, password=password)
            if user_obj and user_obj.is_superuser:
                auth.login(request, user_obj)
                return redirect('dashboard:index')
            
            messages.error(request,'Inavlid Password')
            return redirect('dashboard:login')
            
        return render(request,'dashboard/login.html')
            

    except Exception as e:
        # print(e)
        messages.error(request,'something wrong...')
        return redirect('dashboard:login')


@login_required
def index(request):
    news = News.objects.all()[:5]
    press = Press.objects.all()[:5]
    return render(request,'dashboard/index.html',{'news':news,
                                                  'press':press
                                                  })

@login_required
def userlogout(request):
    auth.logout(request)
    messages.info(request,"logout successfully..")
    return redirect('dashboard:login')


@login_required
def news(request):
    allnews = News.objects.all().order_by('id')
    return render(request,'dashboard/news.html',{'allnews':allnews})

@login_required
def newsdetails(request, slug):
    news = News.objects.get(news_slug= slug)
    return render(request,'dashboard/view.html',{'news':news})


@login_required
def newsupdate(request,slug):
    news = get_object_or_404(News, news_slug= slug)
    return render(request,'dashboard/updateform.html',{'news':news})


@login_required 
def update_news(request):
    if request.method == "POST":
        newsid= request.POST['newsid']
        news = get_object_or_404(News, id = newsid)
        news.title = request.POST['title']
        news.discriptions = request.POST['discription']
        news.image= request.FILES['image']
        news.save()
        messages.success(request,'news update successfully...')
        return render("dashboard:news")


# class NewsUpdate(UpdateView):
#     model = News
#     fields = [
#         "title",
#         "image",
#         "discriptions"
#     ]
#     slug_field = 'news_slug'
#     slug_url_kwarg = 'news_slug'
#     template_name="dashboard/updateform.html"
#     success_url = '/dashboard/news'



@login_required
def create(request):
    if request.method == "POST":
        title = request.POST['title']
        discription = request.POST['discription']
        print(discription)
        image = request.FILES['image']
        if validate_file(image):
            new_news = News(title = title,
                            image = image,
                            discriptions = discription
                            )
            new_news.save()
            messages.success(request,"create successfully..")
            return redirect('dashboard:news')
        else:
            messages.warning(request,'file not match...')
            return render(request,'dashboard/createform.html')

    else:
        return render(request,'dashboard/createform.html')
    
def newsdelete(request, slug):
    try:
        news = News.objects.get(news_slug= slug)
        news.delete()
        messages.success(request,'Deleted successfully...')
        return redirect('dashboard:news')
    
    except Exception as e:
        messages.success(request,'objects doesnot found...')
        return redirect('dashboard:news')
   

@login_required
def events(request):
    if request.method == "POST":
        pass
    else:
        allevents = Event.objects.all().order_by('id')
        return render(request,'dashboard/events.html',{'events':allevents})

@login_required
def uppdateevents(request, slug):
    event = Event.objects.get(event_slug= slug)
    if request.method =="POST":
        event.title = request.POST['title']
        print(request.FILES['image'])
        if request.FILES['image']:
            event.image = request.FILES['image']
        event.discriptions = request.POST['discription']
        event.save()
        messages.success(request,"update successfully..")
        return redirect('dashboard:events')
    else:
        return render(request,'dashboard/eventupdateform.html',{'event':event})
    
@login_required
def viewevent(request,slug):
    try:
        event = Event.objects.get(event_slug = slug)
        return render(request,'dashboard/eventview.html',{'event':event})
    
    except Exception as e:
        print(e)
        messages.warning(request,"event doesnot exites.")
        return redirect('dashboard:events')

@login_required
def create_event(request):
    if request.method == "POST":
        title = request.POST['title']
        discription = request.POST['discription']
        image = request.FILES['image']
        if validate_file(image):
            new_event = Event(title = title,
                            image = image,
                            discriptions = discription
                            )
            new_event.save()
            messages.success(request,"update successfully..")
            return redirect('dashboard:events')
        else:
            messages.warning(request,'file not match...')
            return render(request,'dashboard/eventcreate.html')

    else:
        return render(request,'dashboard/eventcreate.html')
       

@login_required 
def deleteevent(request, slug):
    try:
        event = Event.objects.get(event_slug = slug)
        event.delete()
        messages.info(request,'event deleted...')
        return redirect('dashboard:events')
    except Exception as e:
        print(e)
        messages.warning(request,'not found...')
        return redirect('dashboard:events')



@login_required
def press(request):
    allpress= Press.objects.all().order_by('id')
    return render(request,'dashboard/press.html',{'presses':allpress})


@login_required
def create_press(request):
    if request.method == "POST":
        title = request.POST['title']
        discription = request.POST['discription']
        image = request.FILES['image']
        if validate_file(image):
            new_press = Press(title = title,
                            image = image,
                            discriptions = discription
                            )
            new_press.save()
            messages.success(request,"create successfully..")
            return redirect('dashboard:press')
        else:
            messages(request,'file not match...')
            return render(request,'dashboard/createpress.html')

    else:
        return render(request,'dashboard/createpress.html')
    

@login_required 
def viewpress(request, slug):
    press = Press.objects.get(press_slug= slug)
    return render(request,'dashboard/pressview.html',{'press':press})

@login_required
def updatepress(request, slug):
    if request.method =="POST":
        try:
            press = Press.objects.get(press_slug= slug)
            press.title = request.POST['title']
            if validate_file(request.FILES['image']):
                press.image = request.FILES['image']
            press.discriptions = request.POST['discription']
            press.save()
            messages.success(request,'update successfully...')
            return redirect('dashboard:press')
            
        except Exception as e:
            print(e)
            messages.warning(request,'something wrong....')
            return redirect('dashboard:press')

    else:
        try:
            press = Press.objects.get(press_slug= slug)
            return render(request,'dashboard/pressupdate.html',{'press':press})
        
        except Exception as e:
            print(e)
            messages.warning(request,'some thing wrong..')
            return redirect("dashboard:press")

@login_required 
def deletepress(request, slug):
    try:
        press = Press.objects.get(press_slug = slug)
        press.delete()
        messages.info(request,'press deleted...')
        return redirect('dashboard:press')
    except Exception as e:
        print(e)
        messages.warning(request,'not found...')
        return redirect('dashboard:press')

@login_required
def executivemember(request):
    members = ExecutiveMember.objects.all()
    return render(request,'dashboard/executivemember.html',{'members':members})



@login_required
def updatemember(request):
    if request.method == "POST":
        id = request.POST['memberid']
        member = ExecutiveMember.objects.get(id = id)
        member.full_name= request.POST['fullname']
        member.position =request.POST['position']
        member.phone_number = request.POST['phone']
        if validate_file(request.FILES['image']):
            member.image = request.FILES['image']
            member.save()
            messages.success(request,"update successfully..")
            return redirect('dashboard:executivemember')
        else:
            messages.warning(request,'something wrong !..')
            return redirect('dashboard:executivemember')
        
def create_new_member(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        position = request.POST['position']
        phone = request.POST['phone']
        
        
                
        if validate_file(request.FILES['image']):
            image = request.FILES['image']
            new_member = ExecutiveMember(full_name = fullname,
                            image = image,
                            position = position,
                            phone_number = phone
                            )
            new_member.save()
            messages.success(request,"new member added...")
            return redirect('dashboard:executivemember')
        else:
            messages(request,'file not match...')
            return redirect('dashboard:executivemember')

    else:
        return redirect('dashboard:executivemember')

@login_required
def deleteExecutiveMember(request):
    if request.method == "POST":
        id = request.POST['memberid']
        try:
            related_member = ExecutiveMember.objects.get(id= id)
            related_member.delete()
            messages.success(request,'Deleted...')
            return redirect("dashboard:executivemember")
        except Exception as e:
            print(e)
            messages.warning(request,'something wrong !!!')
            return redirect("dashboard:executivemember")


@login_required
def verified_ordinary_member(request):
    ordinary_member = OrdinaryMember.objects.filter(status="verify")
    print(ordinary_member)
    return render(request,'dashboard/verified_member.html',{'ordinary_member':ordinary_member})


@login_required
def view_ordinary_member(request):
    if request.method =="POST":
        id = request.POST['memberid']
        member_details = OrdinaryMember.objects.get(id=id)
        return render(request,'dashboard/ordinary_details.html',{'details':member_details})

@login_required
def ordinarymember_unrified(request):
    ordinary_member = OrdinaryMember.objects.filter(status="not_verify")
    if request.method=="POST":
        id = request.POST['memberid']
        status = request.POST['status']
        details = OrdinaryMember.objects.get(id = id)
        if status == "verify":
            details.status=status
            details.save()
            messages.info(request,'changes successfulyy..')
            return render(request,'dashboard/ordinary_member.html',{'ordinary_member':ordinary_member})
        else:
            return render(request,'dashboard/ordinary_member.html',{'ordinary_member':ordinary_member})
    else:
        return render(request,'dashboard/ordinary_member.html',{'ordinary_member':ordinary_member})

@login_required
def ordinary_delete(request):
    id = request.POST['memberid']
    ordinary_mem = OrdinaryMember.objects.get(id = id)
    ordinary_mem.delete()
    messages.info(request,'Member Delete Successfully..')
    return redirect('dashboard:verifi_member')

@login_required
def unverifydetails(request):
    id = request.POST['memberid']
    
    details = OrdinaryMember.objects.get(id = id)
    return render(request,'dashboard/ordinary_unverify_details.html',{'details':details})

def unverified_delete(request):
    id = request.POST['memberid']
    member = OrdinaryMember.objects.get(id =id)
    member.delete()
    messages.success(request,'delete succssfully..')
    return redirect('dashboard:ordinary_member_unverifed')

@login_required
def about(request,slug):
    about_ctg= About.objects.get(about_slug=slug)
    try:
        aboutdata = AboutUs.objects.get(category= about_ctg)
        return render(request,'dashboard/about.html',{'aboutdata':aboutdata})
    except Exception as e:
        print(e)
    return redirect("dashboard:index")

def updateabout(request):
    if request.method == "POST":
        category = request.POST['id']
        about_ctg= About.objects.get(title=category)
        aboutdata = AboutUs.objects.get(category= about_ctg)
        aboutdata.title = request.POST['title']
        aboutdata.discription = request.POST['discription']
        image = request.FILES['image']
        if validate_file(image):
            aboutdata.image = image
            aboutdata.save()
            messages.success(request,'update successfully...')
            return render(request,'dashboard/about.html',{'aboutdata':aboutdata})
        else:
            messages.warning(request,'something wrong !!')
            return render(request,'dashboard/about.html',{'aboutdata':aboutdata})
        
@login_required
def manifesto(request):
    if request.method == "POST":
        image = request.FILES['image']
        if validate_file(image):
            newdata = Manifesto(image = image)
            newdata.save()
            messages.success(request,'upload successfulyy..')
            return redirect('dashboard:manifesto')

    else:
        manifesto = Manifesto.objects.all()
        return render(request,'dashboard/manifeston.html',{'manifesto':manifesto})

@login_required
def deletemanifesto(request):
    if request.method == "POST":
        id = request.POST['id']
        data = Manifesto.objects.get(id =id)
        data.delete()
        return redirect('dashboard:manifesto')


@login_required
def createmanifesto(request):
    return render(request,'dashboard/createnewmanifesto.html')



@login_required
def general_info(request):
    if request.method =="POST":
        contactinfo = ContactInfo.objects.first()
        contactinfo.phone_number = request.POST['number']
        contactinfo.email=request.POST['email']
        contactinfo.address=request.POST['location']
        contactinfo.facebook_url=request.POST['facebookurl']
        contactinfo.instagram_url=request.POST['instaurl']
        contactinfo.tiktok_url=request.POST['tiktok']
        contactinfo.twitter_url=request.POST['twitter']
        contactinfo.save()
        messages.success(request,'update successfully..')
        return redirect('dashboard:general_info')
    else:
        contactinfo = ContactInfo.objects.first()
        return render(request,'dashboard/generalinfo.html',{'contactinfo':contactinfo})


def bankdetails(request):
    if request.method =="POST":
        bankdetails = BankDetails.objects.first()
        bankdetails.bank_name=request.POST['bankname']
        bankdetails.account_number=request.POST['accountnumber']
        bankdetails.branch_name=request.POST['branchname']
        image = request.FILES['qrcode']
        if validate_file(image):
            bankdetails.qr_code =image
            bankdetails.save()
            messages.success(request,'update successfully...')
            return redirect('dashboard:bankdetails')
        else:
            messages.warning(request,'Something wrong please try again..')
            return redirect('dashboard:bankdetails')
    else:
        bankdetails = BankDetails.objects.first()
        return render(request,'dashboard/bankdetail.html',{'bankdetails':bankdetails})


@login_required
def gallery(request):
    if request.method == "POST":
        id = request.POST['id']
        image = request.FILES['image']
        title =Gallery.objects.get(id =id)
        print(title)
        obj= Image.objects.create(title= title, image=image)
        print(obj)
        messages.success(request,'Image added...')
        return redirect("dashboard:gallery")
        

    else:
        gallery = Gallery.objects.all()
        return render(request,'dashboard/gallery1.html',{'gallery':gallery})

@login_required
def editgallery(request,slug):
    image_ctg= Gallery.objects.get(img_slug=slug)
    imges = Image.objects.filter(title= image_ctg)
    return render(request,'dashboard/galleryedit.html',{'images':imges})


@login_required
def deleteimage(request):
    if request.method == "POST":
        id  = request.POST['id']
        image_title = request.POST['img_slug']
        print(image_title)
        image =Image.objects.get(id = id)
        image.delete()
        messages.warning(request,'Image Delete successfully..')
        image_ctg= Gallery.objects.get(title=image_title)
        imges = Image.objects.filter(title= image_ctg)
        return render(request,'dashboard/galleryedit.html',{'images':imges})

@login_required
def deletealbum(request):
    if request.method == "POST":
        id = request.POST['id']
        related_image = Gallery.objects.get(id =id)
        related_image.delete()
        messages.success(request,"Album delete successfully..")
        return redirect("dashboard:gallery")


@login_required
def createnewalbum(request):
    if request.method=="POST":
        name = request.POST['albumname']
        galler_title = Gallery(title = name)
        galler_title.save()
        messages.success(request,"Album create successfully..")
        return redirect("dashboard:gallery")
    

@login_required
def bannar_image(request):
    image = BannarImage.objects.first()
    if request.method == "POST":
        image= request.FILES['image']
        if validate_file(image):
            obj = BannarImage(image = image)
            obj.save()
            messages.success(request,"Image uploaded successfully...")
            return redirect("dashboard:bannar_image")
        else:
            messages.warning(request,"something wrong...")
            return redirect("dashboard:bannar_image")
    else:
        return render(request,'dashboard/bannarimage.html',{'image':image})
    

@login_required
def delete_bannar_image(request):
    if request.method == "POST":
        id = request.POST['id']
        related_image = BannarImage.objects.get(id =id)
        related_image.delete()
        messages.warning(request,"image deleted sucessfully")
        return redirect("dashboard:bannar_image")
    

from collections import Counter
@login_required
def notification(requset):
    notice_for_today = NoticeBoard.objects.first()
    if requset.method == "POST":
        content = requset.POST['discription']
        print(len(content))
        if len(content.split()) <=100:
            obj=  NoticeBoard(notic = content)
            obj.save()
            messages.success(requset,"notice update sucessfully")
            return redirect("dashboard:notification")
        else:
            messages.warning(requset,"100 characters only !!!")
            return redirect("dashboard:notification")
    else:
        return render(requset,'dashboard/notification.html',{'notice_day':notice_for_today})

@login_required
def videogallery(request):
    if request.method == "POST":
        video_url = request.POST['url']
        discription = request.POST['discription']
        obj = Video(video_url= video_url,
                    discriptions =discription
                    )
        obj.save()
        messages.success(request,"video added successfully...")
        return redirect("dashboard:videogallery")
    else:
        videos = Video.objects.all()
        return render(request,'dashboard/video.html',{'videos':videos})

@login_required
def delete_video(request):
    if request.method == "POST":
        id = request.POST['videoid']
        video = Video.objects.get(id = id)
        video.delete()
        messages.success(request,"video deleted successfully...")
        return redirect("dashboard:videogallery")




@login_required
def branchlist(request):
    if request.method == "POST":
        branch_name_nepali = request.POST['branch_name_nepali']
        branch_name_english = request.POST['branch_name_english']
        obj = Branch(branch_name_nepali= branch_name_nepali, branch_name_english= branch_name_english)
        obj.save()
        messages.info(request,"New branch added !")
        allbranch = Branch.objects.all()
        return render(request,'dashboard/branch.html',{'branchlist':allbranch})
    allbranch = Branch.objects.all()
    return render(request,'dashboard/branch.html',{'branchlist':allbranch})



@login_required
def deletebranch(request):
    if request.method == "POST":
        id = request.POST['branchid']
        branch = Branch.objects.get(id = id)
        branch.delete()
        messages.info(request,"Branch Deleted successfully !")
        return redirect('dashboard:branchlist')
    

@login_required
def editbranch(request):
    id = request.POST['branchid']
    branch = Branch.objects.get(id = id)
    branch.branch_name_nepali= request.POST['branch_name_nepali']
    branch.branch_name_english = request.POST['branch_name_english']
    branch.save()
    messages.info(request,"Branch Name updated successfully..")
    return redirect("dashboard:branchlist")