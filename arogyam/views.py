from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from .models import ArogyamSlider,ArogyamFliper,ArogyamService,ArogyamBrand,Event,Contact,FilesAdmin

# Create your views here.

def index(request): 
    slider=ArogyamSlider.objects.all()
    fliper=ArogyamFliper.objects.all()
    service=ArogyamService.objects.all()
    brand=ArogyamBrand.objects.all()
    event=Event.objects.all()
    context = {'slider':slider,'fliper':fliper,'service':service,'brand':brand,'event':event}
    return render(request,'arogyam/index.html',context)

def eventHome(request):
    event = Event.objects.all()
    params = {'event':event}
    return render(request, "arogyam/event/eventHome.html", params)

def eventPost(request, slug): 
    post=Event.objects.filter(slug=slug).first()
    context={'post':post}
    return render(request, "arogyam/event/eventPost.html", context)

def contactus(request):
  if request.method == "POST":
      name = request.POST.get('name')
      mobileno = request.POST.get('mobileno')
      email = request.POST.get('email')
      messages = request.POST.get('messages')
      subject = request.POST.get('subject')
      contact = Contact(name=name, mobileno=mobileno,email=email,messages=messages, subject=subject, createdon=datetime.today())
      contact.save()
      return redirect('contact')
  else:   
      return render(request,"arogyam/contactus.html")

def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(),content_type="application/adminfile")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response

    raise Http404

def fileDownload(request): 
    context={'file':FilesAdmin.objects.all()}
    return render(request,'arogyam/download.html',context)

def video(request): 
    context={'file':Video.objects.all()}
    return render(request,'arogyam/video.html',context)
