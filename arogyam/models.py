from django.db import models
from django.utils.timezone import now
# Create your models here.


class ArogyamSlider(models.Model):
    slider_id = models.AutoField
    slider_title = models.CharField(max_length=50)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='static/arogyam/slider', default="")
  

    def __str__(self):
        return self.slider_title

class ArogyamFliper(models.Model):
    fliper_id = models.AutoField
    fliper_title = models.CharField(max_length=50)
    desc = models.TextField(default="")
    image = models.ImageField(upload_to='static/arogyam/fliper', default="")

    def __str__(self):
        return self.fliper_title

class ArogyamService(models.Model):
    service_id = models.AutoField
    service_title = models.CharField(max_length=50)
    slug=models.CharField(max_length=50, default="")
    desc = models.TextField(default="")
    image = models.ImageField(upload_to='static/arogyam/service', default="")

    def __str__(self):
        return self.service_title

class ArogyamBrand(models.Model):
    brand_id = models.AutoField
    brand_title = models.CharField(max_length=50)
    slug=models.CharField(max_length=50, default="")
    desc = models.TextField(default="")
    image = models.ImageField(upload_to='static/arogyam/brand', default="")

    def __str__(self):
        return self.brand_title

class Event(models.Model):
    evnet_id = models.AutoField
    evnet_title = models.CharField(max_length=50)
    event_author = models.CharField(max_length=50, default="")
    slug=models.CharField(max_length=50, default="")
    desc = models.TextField(default="")
    pub_date = models.DateField()
    image = models.ImageField(upload_to='static/arogyam/event', default="")

    def __str__(self):
        return self.evnet_title

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(null=True,max_length=255, blank=False)
    mobileno = models.CharField(null=True,max_length=13, blank=False)
    messages = models.CharField(max_length=255)
    createdon = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
    def __str__(self):
        return self.email


class FilesAdmin(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    content=models.CharField(max_length=255,default="")
    adminfile = models.FileField(upload_to='media/cancercare/pdf', default="")
    image = models.ImageField(upload_to='static/cancercare/pdf', default="")
    def __str__(self):
        return self.title 

class Video(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    content=models.CharField(max_length=255,default="")
    def __str__(self):
        return self.title 

