from django.db import models
from django.utils.timezone import now


class Advisor(models.Model):
    id = models.AutoField(primary_key=True)
    advisor_name = models.CharField(max_length=50)
    advisor_email = models.CharField(max_length=70, default="")
    advisor_phone = models.CharField(max_length=70, default="")
    messages = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.advisor_name


class Blog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    content=models.TextField()
    image = models.ImageField(upload_to='static/diabetescare/blog', default="")
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
    adminfile = models.FileField(upload_to='media/diabetescare/pdf', default="")
    image = models.ImageField(upload_to='static/diabetescare/pdf', default="")
    def __str__(self):
        return self.title 

class Video(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    content=models.CharField(max_length=255,default="")
    def __str__(self):
        return self.title 

class Disease(models.Model):
    disease_id = models.AutoField
    disease_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    slug=models.CharField(max_length=130,default="")
    content=models.TextField(default="")
    desc = models.TextField(default="")
    pub_date = models.DateField()
    image = models.ImageField(upload_to='static/diabetescare/disease', default="")

    def __str__(self):
        return self.disease_name

class Testimonial(models.Model):
    testimonial_id = models.AutoField
    testimonial_name = models.CharField(max_length=50)
    content=models.TextField(default="")
    
    def __str__(self):
        return self.testimonial_name

class Event(models.Model):
    evnet_id = models.AutoField
    evnet_title = models.CharField(max_length=50)
    event_author = models.CharField(max_length=50, default="")
    slug=models.CharField(max_length=50, default="")
    desc = models.TextField(default="")
    pub_date = models.DateField()
    image = models.ImageField(upload_to='static/diabetescare/event', default="")

    def __str__(self):
        return self.evnet_title

class Slider(models.Model):
    slider_id = models.AutoField
    slider_title = models.CharField(max_length=50)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='static/diabetescare/slider', default="")

    def __str__(self):
        return self.slider_title