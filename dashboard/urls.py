from django.urls import path
from . import views
app_name= 'dashboard'

urlpatterns = [
    path('',views.login, name='login'),

    path('about/<slug:slug>', views.about, name='about'),
    path('about/update/about', views.updateabout, name='updateabout'),
    path('manifesto', views.manifesto, name='manifesto'),
    path('manifesto/delete', views.deletemanifesto, name="deletemanifesto"),
    path('manifesto/create', views.createmanifesto, name='createmanifesto'),
    path('generalinfo', views.general_info, name='general_info'),
    path('bank-details', views.bankdetails, name='bankdetails'),

    path('index',views.index, name='index'),
    path('logout', views.userlogout, name='logout'),
    path('news', views.news, name='news'),
    path('news/create', views.create, name='create_news'),
    path('news/<slug:slug>', views.newsdetails, name='newsdetail'),
    path('news/update/<slug:slug>', views.newsupdate, name='news_update'),
    path('news/update', views.update_news, name='update_news'),
    path('news/<slug:slug>/delete', views.newsdelete, name='news_delete'),
   
    path('events', views.events, name='events'),
    path('event/create', views.create_event, name='event_create'),
    path('event/<slug:slug>', views.uppdateevents, name='update_evente'),
    path('event/view/<slug:slug>', views.viewevent, name='event_view'),
    path('evente/delete/<slug:slug>', views.deleteevent, name='delete_event'),

    path('press', views.press, name='press'),
    path('press/view/<slug:slug>', views.viewpress, name='viewpress'),
    path('press/update/<slug:slug>', views.updatepress, name='updatepress'),
    path('press/delete/<slug:slug>', views.deletepress, name='deltepress'),
    path('press/create', views.create_press, name='create_press'),


    path('executive_member', views.executivemember, name='executivemember'),
    path('executive_member/update', views.updatemember, name="updatemember"),
    path('executive_member/create', views.create_new_member, name="create_new_mem"),
    path('executive_member/delete', views.deleteExecutiveMember, name="exe_delete"),

    path('ordinary_member/verify', views.verified_ordinary_member, name="verifi_member"),
    path('ordinary_member/unverify', views.ordinarymember_unrified, name="ordinary_member_unverifed"),
    path('ordinary_delte', views.ordinary_delete,name="delete_ordinary"),
    path('ordinary_details', views.unverifydetails, name='unverifed_details'),
    path('unordinary_delete', views.unverified_delete, name="unordinary_delete"),
    path('ordinary/verify_details', views.view_ordinary_member, name='ordinary_details'),
    path('gallery', views.gallery, name='gallery'),
    path('gallery/<slug:slug>', views.editgallery, name="editgallery"),
    path('gallery/image/delete', views.deleteimage, name='deleteimage'),
    path('ablum/delete', views.deletealbum, name='deletealbum'),
    path('album/create', views.createnewalbum, name="createnewalbum"),
    path('bannar_image', views.bannar_image, name='bannar_image'),
    path('bannar/delete', views.delete_bannar_image, name="delete_bannar_image"),
    path('notification', views.notification, name='notification'),
    path('video-gallery', views.videogallery, name='videogallery'),
    path('video/delete', views.delete_video, name='delete_video'),
    path('branch-list', views.branchlist, name='branchlist'),
    path('branch/delete', views.deletebranch, name='deletebranch'),
    path('branch/edit', views.editbranch, name='editbranch'),
]
