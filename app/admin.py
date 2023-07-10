from django.contrib import admin
from . models import News,Press,Event,Gallery, Image,Video,ExecutiveMember,\
    OrdinaryMember,About,AboutUs,ContactInfo,BankDetails,Manifesto,Keyword,Discription,\
    Auth,BannarImage,NoticeBoard,Branch


admin.site.register(Keyword)
admin.site.register(Discription)
admin.site.register(Auth)

admin.site.register(NoticeBoard)


class BannarImageAdmin(admin.ModelAdmin):
    model= BannarImage
    list_display = ['id','image']
admin.site.register(BannarImage,BannarImageAdmin)


class NewsAdmin(admin.ModelAdmin):
    model :News
    list_display =['title','image']
admin.site.register(News, NewsAdmin)


class PressAdmin(admin.ModelAdmin):
    model :Press
    list_display= ['title','image']
admin.site.register(Press,PressAdmin)

class EventAdmin(admin.ModelAdmin):
    model :Event
    list_display= ['title','image']
admin.site.register(Event,EventAdmin)


class ImageAdmin(admin.TabularInline):
    model=Image

class GalleryAdmin(admin.ModelAdmin):
    inlines =[
        ImageAdmin
    ]
    list_display =['title']
admin.site.register(Gallery, GalleryAdmin)

class VideoAdmin(admin.ModelAdmin):
    model =Video
    list_display = ['id','video_url','discriptions']
admin.site.register(Video,VideoAdmin)

class ExecutiveMemberAdmin(admin.ModelAdmin):
    model=ExecutiveMember
    list_display =['full_name','position','phone_number']
admin.site.register(ExecutiveMember, ExecutiveMemberAdmin)

class OrdinaryMemberAmin(admin.ModelAdmin):
    model=OrdinaryMember
    list_display =['fullname','phone_number','email','image','father_name','mother_name','documents','status']
    list_filter = ['status',]

    def has_add_permission(self, request, obj=None):
        return True
    
    def has_delete_permission(self, request, obj=None):
        return True
    
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
    
admin.site.register(OrdinaryMember,OrdinaryMemberAmin)



class AboutDetailsAdmin(admin.ModelAdmin):
    model = AboutUs
    list_display = ['category','title','image']

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
    
admin.site.register(AboutUs,AboutDetailsAdmin)

# class AboutAdmin(admin.ModelAdmin):
#     model= About
#     list_display = ['title']
# admin.site.register(About, AboutAdmin)


class ContactInfoAdmin(admin.ModelAdmin):
    model =ContactInfo
    list_display =['address','phone_number','email','facebook_url','twitter_url','instagram_url','tiktok_url']

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
    
admin.site.register(ContactInfo,ContactInfoAdmin)



class BankDetailsAdmin(admin.ModelAdmin):
    model=BankDetails
    list_display =['bank_name','account_number','branch_name','qr_code']

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
    
admin.site.register(BankDetails,BankDetailsAdmin)


class ManifestoAdmin(admin.ModelAdmin):
    model=Manifesto
    list_display =['id','image']

admin.site.register(Manifesto,ManifestoAdmin)


class BranchAdmin(admin.ModelAdmin):
    model =  Branch
    list_display = ['branch_name_nepali','branch_name_english']
admin.site.register(Branch, BranchAdmin)