from django.db import models
from django.utils.timezone import now

class Slider(models.Model):
    slider_id = models.AutoField
    slider_title = models.CharField(max_length=50)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='static/arogyaveda/slider', default="")

    def __str__(self):
        return self.slider_title

class Blog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    content=models.TextField()
    image = models.ImageField(upload_to='static/cancercare/blog', default="")
    title2=models.CharField(max_length=255,default="")
    content2=models.TextField(default="")
    def __str__(self):
        return self.title + " by " + self.author

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