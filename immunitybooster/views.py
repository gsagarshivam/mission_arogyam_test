from django.shortcuts import render,redirect
from .models import Advisor
from .models import Blog
from .models import Testimonial
from .models import Disease
from .models import Slider
from .models import Contact
from .models import FilesAdmin
from arogyam.models import Event
from arogyam.models import ArogyamBrand
from .models import Video
from math import ceil
from io import BytesIO
from django.contrib import messages
from datetime import datetime
from django.template.loader import get_template
# Create your views here.
from django.http import HttpResponse
def index(request): 
    file=Blog.objects.all()
    disease=Disease.objects.all()
    event=Event.objects.all()
    slider=Slider.objects.all()
    brand=ArogyamBrand.objects.all()
    context={'file':file ,'disease':disease,'event':event,'slider':slider,'brand':brand}
    return render(request,'immunitybooster/index.html',context)

def blogHome(request): 
    allBlog= Blog.objects.all()
    context={'allBlog': allBlog}
    return render(request, "immunitybooster/blog/blogHome.html", context)

def advisor(request):
    if request.method=="POST":
        advisor_name=request.POST.get('advisor_name', '')
        advisor_email=request.POST.get('advisor_email', '')
        advisor_phone=request.POST.get('advisor_phone', '')
        messages=request.POST.get('messages', '')
        advisor = Advisor(advisor_name=advisor_name, advisor_email=advisor_email, advisor_phone=advisor_phone, messages=messages)
        advisor.save()
    return redirect('ShopHome')

def blogPost(request, slug): 
    post=Blog.objects.filter(slug=slug).first()
    context={'post':post}
    return render(request, "immunitybooster/blog/blogPost.html", context)


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
      return render(request,"immunitybooster/contactus.html")

def download(request,path):
	file_path=os.path.join(settings.MEDIA_ROOT,path)
	if os.path.exists(file_path):
		with open(file_path,'rb')as fh:
			response=HttpResponse(fh.read(),content_type="application/adminfile")
			response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
			return response

	raise Http404


def diseaseHome(request): 
    catprods = Disease.objects.all()
    params = {'catprods':catprods}
    return render(request, "immunitybooster/diseases/diseaseHome.html", params)

def diseasePost(request, slug): 
    post=Disease.objects.filter(slug=slug).first()
    context={'post':post}
    return render(request, "immunitybooster/diseases/diseasePost.html", context)

def fileDownload(request): 
    context={'file':FilesAdmin.objects.all()}
    return render(request,'immunitybooster/download.html',context)

def video(request): 
    context={'file':Video.objects.all()}
    return render(request,'immunitybooster/video.html',context)

def blogslug(request): 
    context={'file':Blog.objects.all()}
    return render(request,'immunitybooster/base.html',context)

def eventHome(request):
    event = Event.objects.all()
    params = {'event':event}
    return render(request, "immunitybooster/event/eventHome.html", params)

def eventPost(request, slug): 
    post=Event.objects.filter(slug=slug).first()
    context={'post':post}
    return render(request, "immunitybooster/event/eventPost.html", context)


