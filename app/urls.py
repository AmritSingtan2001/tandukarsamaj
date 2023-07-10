from django.urls import path
from . import views
from .views import IndexList, NewDetailsView,PressDetailViews,EventDetailView,\
    NewsPressListView,EventListView,GalleryListViews,GalleryDetailView,\
    VideoListView,Members,AboutDetailtView,ManifestonList,LifeTimeMember,OrdinaryMemberlistView,BranchListView

urlpatterns = [
    path('', IndexList.as_view(), name='index'),
    path('about/<slug:about_slug>',AboutDetailtView.as_view(), name='about' ),
    path('news',NewsPressListView.as_view(), name='news' ),
    path('news/<slug:news_slug>',NewDetailsView.as_view(), name='news-details'),
    path('press/<slug:press_slug>',PressDetailViews.as_view(), name='press-details'),
    path('event', EventListView.as_view(), name='events'),
    path('event/<slug:event_slug>', EventDetailView.as_view(), name='event-details'),
    path('gallery', GalleryListViews.as_view(), name="gallery"),
    path('gallery/<slug:img_slug>', GalleryDetailView.as_view(), name="gallery-details"),
    path('videos', VideoListView.as_view(), name='videos'),
    path('members', Members.as_view(), name='members'),
    path('members/life-time-members', LifeTimeMember.as_view(), name='lifetimemembers'),
    path('members/ordinary-members', OrdinaryMemberlistView.as_view(), name='ordinaryMember'),
    # path('registration', views.registration, name='registration'),
    path('donation', views.donation, name='donation'),
    path('ordeinary/registration', views.ordinary_member_registration, name='registration'),
    path('manifeston', ManifestonList.as_view() , name='manifeston'),
    path('branch', BranchListView.as_view() , name='branchlist'),



    # translate language url
    path("set_language/<str:language>", views.set_language, name="set-language"),
    # end tanslate language url 

    # path('about',views.about, name='about'),
    path('vission', views.vission, name='vission'),
    path('executive-members', views.executivemembers, name='exe-members'),
    
    path('notice', views.notice, name='notice'),
    
    path('notice/details', views.notice_details, name='notice_details'),
    # path('gallery', views.imagegallery, name='gallery'),
    path('gallery/acd-images', views.innerimage, name='inner-gallery'),
    # path('videos', views.videogallery, name='videos'),
    path('transparency', views.transparency, name='transparency'),
    path('login', views.login, name='login'),
 
]

