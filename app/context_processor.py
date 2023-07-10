from . models import About,ContactInfo,BankDetails,BannarImage,Video

def aboutctg(request):
    about = About.objects.all()
    return{
        'aboutctg':about
    }

def contact(request):
    contact_info = ContactInfo.objects.first()
    return {
        'contact':contact_info
    }


def bankdetails(request):
    bank_details = BankDetails.objects.first()
    return {
        'bank_details':bank_details
    }
    
def bannarimage(request):
    bannar_image = BannarImage.objects.first()
    return ({
        'bannar_image':bannar_image
    })
    
    
def first_video(request):
    video = Video.objects.first()
    return({
        'videos':video
    })