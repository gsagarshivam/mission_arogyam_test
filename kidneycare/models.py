from django.db import models
from django.utils.timezone import now

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='image/kidneycare', default="")

    def __str__(self):
        return self.product_name




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
    image = models.ImageField(upload_to='static/kidneycare/blog', default="")
    title2=models.CharField(max_length=255,default="")
    content2=models.TextField(default="")
    def __str__(self):
        return self.title + " by " + self.author



class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    username=models.CharField(max_length=255, default="")
    useremail = models.CharField(max_length=70, default="")
    userphone = models.CharField(max_length=70, default="")
    comment=models.TextField(default="")
    post=models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.username

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
    adminfile = models.FileField(upload_to='media/kidneycare/pdf', default="")
    image = models.ImageField(upload_to='static/kidneycare/pdf', default="")
    def __str__(self):
        return self.title 

class KidneycareVideo(models.Model):
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
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='static/kidneycare/disease', default="")

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
    image = models.ImageField(upload_to='static/kidneycare/event', default="")

    def __str__(self):
        return self.evnet_title

class Slider(models.Model):
    slider_id = models.AutoField
    slider_title = models.CharField(max_length=50)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='static/kidneycare/slider', default="")

    def __str__(self):
        return self.slider_title


    
    


