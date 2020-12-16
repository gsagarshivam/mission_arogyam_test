from django.shortcuts import render,redirect
from datetime import datetime
from .models import Slider,Blog,Contact,FilesAdmin,Video
from django.template.loader import get_template
from arogyam.models import Event
from arogyam.models import ArogyamService
# Create your views here.
from django.http import HttpResponse

def index(request): 
    slider=Slider.objects.all()
    file=Blog.objects.all()
    event=Event.objects.all()
    service=ArogyamService.objects.all()
    context={'slider':slider,'service':service,'file':file,'event':event}
    return render(request,'rupam/index.html',context)

def blogHome(request): 
    allBlog= Blog.objects.all()
    context={'allBlog': allBlog}
    return render(request, "rupam/blog/blogHome.html", context)

def blogPost(request, slug): 
    post=Blog.objects.filter(slug=slug).first()
    context={'post':post}
    return render(request, "rupam/blog/blogPost.html", context)

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
      return render(request,"rupam/contactus.html")

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
    return render(request,'rupam/download.html',context)

def video(request): 
    context={'file':Video.objects.all()}
    return render(request,'rupam/video.html',context)