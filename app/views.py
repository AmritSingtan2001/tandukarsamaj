from django.shortcuts import render,get_object_or_404,HttpResponse,redirect
from django.views.generic import ListView,DetailView
from django.contrib import messages
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from . file_handler import validate_file,phone_number_validation
from . models import News,Press,Event,Gallery,Image,Video,ExecutiveMember,\
    About,AboutUs,OrdinaryMember,Manifesto,BannarImage,NoticeBoard, Branch



def error_404(request, exception):
    return render(request, 'dashboard/pagenotfound.html')



def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response


class IndexList(ListView):
    model = News
    template_name ='app/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(IndexList,self).get_context_data(*args, **kwargs)
        context['news'] = News.objects.all()[:4] 
        context['singlepress'] = Press.objects.all()[:1]  
        context['press'] = Press.objects.all()[1:7] 
        context['events'] = Event.objects.all()[:4]  
        context['bannarimage'] = BannarImage.objects.first()
        context['notice'] = NoticeBoard.objects.first()
        return context

class AboutDetailtView(DetailView):
    model = About
    template_name ='app/details-page.html'
    slug_field = 'about_slug'
    slug_url_kwarg = 'about_slug'

    def get_context_data(self, *args, **kwargs):
        context = super(AboutDetailtView,self).get_context_data(*args, **kwargs)
        about_ctg= get_object_or_404(About, about_slug=self.kwargs['about_slug'])   
        context['about']  = about_ctg.category.first()
        return context



class NewDetailsView(DetailView):
    model = News
    template_name ='app/newdetails.html'
    slug_field = 'news_slug'
    slug_url_kwarg = 'news_slug'

    def get_context_data(self, *args, **kwargs):
        context = super(NewDetailsView,self).get_context_data(*args, **kwargs)
        context['news'] = get_object_or_404(News, news_slug=self.kwargs['news_slug'])   
        return context


class PressDetailViews(DetailView):
    
    model= Press
    template_name ='app/pressdetails.html'
    slug_field = 'press_slug'
    slug_url_kwarg = 'press_slug'

    def get_context_data(self, *args, **kwargs):
        context = super(PressDetailViews,self).get_context_data(*args, **kwargs)
        context['press_details'] = get_object_or_404(Press, press_slug=self.kwargs['press_slug'])   
        return context

    
class NewsPressListView(ListView):
    model = News
    template_name ='app/noticenews.html'
    paginate_by = 8

    def get_context_data(self, *args, **kwargs):
        context = super(NewsPressListView,self).get_context_data(*args, **kwargs)
        allnews= News.objects.all()
        news = allnews[1:]
        paginator = Paginator(news, self.paginate_by) 
        page = self.request.GET.get('page')

        try:
            all_news = paginator.page(page)
        except PageNotAnInteger:
            all_news = paginator.page(1)
        except EmptyPage:
            all_news = paginator.page(paginator.num_pages)


        context['firstnews'] = allnews[:1] 
        context['news'] = all_news
        context['lastnews'] =allnews[9:10]
        allpress = Press.objects.all()
        context['firstpress'] = allpress[:1]  
        context['press'] = allpress[1:9] 
        context['lastpress'] =allpress[9:10]
        return context
    

class EventListView(ListView):
    model=Event
    template_name = "app/event.html"
    paginate_by = 8

    def get_context_data(self, *args, **kwargs):
        context = super(EventListView,self).get_context_data(*args, **kwargs)
        allevents = Event.objects.all()
        paginator = Paginator(allevents, self.paginate_by) 
        page = self.request.GET.get('page')

        try:
            events = paginator.page(page)
        except PageNotAnInteger:
            events = paginator.page(1)
        except EmptyPage:
            events = paginator.page(paginator.num_pages)
        
        context['events'] =events
        return context


class EventDetailView(DetailView):
    model= Event
    template_name ='app/pressdetails.html'
    slug_field = 'event_slug'
    slug_url_kwarg = 'event_slug'

    def get_context_data(self, *args, **kwargs):
        context = super(EventDetailView,self).get_context_data(*args, **kwargs)
        context['press_details'] = get_object_or_404(Event, event_slug=self.kwargs['event_slug'])   
        return context

class GalleryListViews(ListView):
    model = Gallery
    template_name ="app/imagegallery.html"
    context_object_name='gallery'

class GalleryDetailView(DetailView):
    model= Gallery
    template_name ='app/inner-gallery.html'
    slug_field = 'img_slug'
    slug_url_kwarg = 'img_slug'

    def get_context_data(self, *args, **kwargs):
        context = super(GalleryDetailView,self).get_context_data(*args, **kwargs)
        image_title = get_object_or_404(Gallery, img_slug=self.kwargs['img_slug'])  
        context['gallery'] = image_title.gallery.all() 
        return context



class VideoListView(ListView):
    model = Video
    template_name ='app/videogallery.html'
    context_object_name='videos'


class Members(ListView):
    model= ExecutiveMember
    template_name= 'app/executivemembers.html'
    context_object_name = 'members'

   


class LifeTimeMember(ListView):
    model = OrdinaryMember
    template_name = 'app/lifetimemembers.html'

    def get_context_data(self, *args, **kwargs):
        context = super(LifeTimeMember,self).get_context_data(*args, **kwargs)
        context['life_time_members'] = OrdinaryMember.objects.filter(status= "verify", membertype ="life time")
        return context
    


class OrdinaryMemberlistView(ListView):
    model = OrdinaryMember
    template_name = 'app/ordinarymembers.html'

    def get_context_data(self, *args, **kwargs):
        context = super(OrdinaryMemberlistView,self).get_context_data(*args, **kwargs)
        context['ordinary_member'] = OrdinaryMember.objects.filter(status= "verify",  membertype ="ordinary" )
        return context
    
class ManifestonList(ListView):
    model= Manifesto
    template_name= 'app/manifesto.html'
    context_object_name = 'manifestos'

def ordinary_member_registration(request):
    if request.method =="POST":
        fullname = request.POST['fullname']
        email = request.POST['email']
        phone_number = request.POST['number']
        grandfathername = request.POST['grandfathername']
        fathername = request.POST['fathername']
        mothername = request.POST['mothername']
        son = request.POST['sonname']
        daughter = request.POST['daughtername']
        temporary_address = request.POST['tempaddress']
        permanent_address = request.POST['per_address']
        country = request.POST['country']
        qualification = request.POST['qualification']
        image = request.FILES['image']
        document = request.FILES['document']
        member_type= request.POST['membertype']
        print(member_type)

        if phone_number_validation(phone_number):
            if validate_file(image):
                if validate_file(document ):
                    member = OrdinaryMember( fullname=fullname,
                                        phone_number=phone_number,
                                        email = email,
                                        grand_father_name= grandfathername,
                                        father_name= fathername,
                                        mother_name= mothername,
                                        son_name=son,
                                        daughter_name=daughter,
                                        temporary_address=temporary_address,
                                        permanent_address=permanent_address,
                                        country=country,
                                        qualification= qualification,
                                        image = image,
                                        documents=document,
                                        membertype = member_type
                                    )
                    
                    member.save()
                    messages.success(request,"form submited successfully....")
                    return render(request,'app/registration.html')
                
                messages.warning(request,'invalid document formate...')
                return render(request,'app/registration.html')
           
            messages.warning(request,'invalid image formate...')
            return render(request,'app/registration.html')

        
        messages.warning(request,'phone containes exact 10 digits and start with 9...')
        return render(request,'app/registration.html')

    else:
        return render(request,'app/registration.html')



class BranchListView(ListView):
    model = Branch
    template_name = 'app/branchlist.html'
    context_object_name ='branchlist'










def about(request):
    return render(request,'app/about.html')


def vission(request):
    return render(request,'app/vission.html')

def executivemembers(request):
    return render(request,'app/executivemembers.html')





def notice(request):
    return render(request,'app/noticenews.html')




def notice_details(request):
    return render(request,'app/details-page.html')


def event(request):
    return render(request,'app/event.html')

def imagegallery(request):
    return render(request,'app/imagegallery.html')

def innerimage(request):
    return render(request,'app/inner-gallery.html')

def videogallery(request):
    return render(request,'app/videogallery.html')

def transparency(request):
    return render(request,'app/transparency.html')

def login(request):
    return render(request,'app/login.html')


def donation(request):
    return render(request,'app/donation.html')